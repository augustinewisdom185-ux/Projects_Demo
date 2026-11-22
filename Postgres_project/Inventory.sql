--Inventory sql database

CREATE DATABASE inventory;

CREATE EXTENSION IF NOT EXISTS "pgcrypto"; -- Enables gen_random_uuid()

CREATE TABLE categories (
    category_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    slug VARCHAR(120) UNIQUE NOT NULL
);

CREATE TABLE warehouses (
    warehouse_id BIGSERIAL PRIMARY KEY,
    w_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    product_id BIGSERIAL PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id BIGINT REFERENCES categories(category_id) ON DELETE SET NULL,
    price NUMERIC(12, 2) NOT NULL CHECK (price >= 0),
    image_url TEXT,
    is_published BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE inventory_level (
    product_id BIGINT REFERENCES products(product_id) ON DELETE RESTRICT,
    warehouse_id BIGINT REFERENCES warehouses(warehouse_id) ON DELETE RESTRICT,
    quantity_on_hand INT NOT NULL DEFAULT 0 CHECK (quantity_on_hand >= 0),
    quantity_reserved INT NOT NULL DEFAULT 0 CHECK (quantity_reserved >= 0),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (product_id, warehouse_id),
    CONSTRAINT chk_available_stock CHECK (quantity_on_hand >= quantity_reserved)
);

CREATE TABLE customer (
    customer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone VARCHAR(30) NOT NULL,
    password_hash TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE customer_address (
    address_id BIGSERIAL PRIMARY KEY,
    customer_id UUID NOT NULL REFERENCES customer(customer_id) ON DELETE CASCADE,
    city VARCHAR(100) NOT NULL,
    neighborhood_or_street TEXT NOT NULL,
    delivery_note TEXT,
    is_default BOOLEAN DEFAULT FALSE
);

CREATE TABLE orders (
    order_id BIGSERIAL PRIMARY KEY,
    order_number VARCHAR(30) UNIQUE NOT NULL,
    customer_id UUID NOT NULL REFERENCES customer(customer_id) ON DELETE RESTRICT,
    shipping_address_id BIGINT NOT NULL REFERENCES customer_address(address_id) ON DELETE RESTRICT,
    status VARCHAR(25) NOT NULL DEFAULT 'PENDING_PAYMENT'
        CHECK (status IN ('PENDING_PAYMENT', 'PAID', 'PROCESSING', 'SHIPPING', 'DELIVERED', 'CANCELLED', 'REFUNDING')),
    total_amount NUMERIC(12, 2) NOT NULL CHECK (total_amount >= 0),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE order_items (
    order_item_id BIGSERIAL PRIMARY KEY,
    order_id BIGINT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id BIGINT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price_at_purchase NUMERIC(12, 2) NOT NULL CHECK (unit_price_at_purchase >= 0)
);

CREATE TABLE payments (
    payment_id BIGSERIAL PRIMARY KEY,
    order_id BIGINT NOT NULL REFERENCES orders(order_id) ON DELETE RESTRICT,
    provider VARCHAR(50) NOT NULL,
    transaction_ref VARCHAR(150) UNIQUE,
    amount NUMERIC(12, 2) NOT NULL CHECK (amount >= 0),
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING'
        CHECK (status IN ('PENDING', 'SUCCESS', 'FAILED', 'REFUNDED')),
    paid_at TIMESTAMPTZ
);

CREATE TABLE stock_movement (
    movement_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    warehouse_id BIGINT NOT NULL REFERENCES warehouses(warehouse_id) ON DELETE RESTRICT,
    order_id BIGINT REFERENCES orders(order_id) ON DELETE SET NULL,
    movement_type VARCHAR(20) NOT NULL
        CHECK (movement_type IN ('RESTOCK', 'CUSTOMER_SALE', 'RETURN', 'ADJUSTMENT')),
    quantity_change INT NOT NULL CHECK (quantity_change <> 0),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_products_category ON products(category_id) WHERE is_published = TRUE;
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_payments_order ON payments(order_id);

-- Allow the app to connect to your database
CREATE ROLE inventory_app WITH LOGIN PASSWORD 'strong_random_password';
GRANT CONNECT ON DATABASE inventory TO inventory_app;

-- Give read/insert/update permissions on all your tables and ID counters
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO inventory_app;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO inventory_app;

-- Make the audit log append-only (matches your singular table name)
REVOKE UPDATE, DELETE ON stock_movement FROM inventory_app;
