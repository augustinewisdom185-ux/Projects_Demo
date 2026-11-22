# Production-Ready E-Commerce & Inventory Database (PostgreSQL)

A scalable, ledger-backed PostgreSQL database schema designed for modern e-commerce applications and multi-warehouse inventory management. Built with strict data integrity, concurrency controls to prevent overselling, idempotent payment tracking, and role-based database security.

---

## Key Features

* **Overselling Prevention (Concurrency Control):** Separates `quantity_on_hand` from `quantity_reserved` with database-level `CHECK` constraints and row-locking (`FOR UPDATE`) support during checkout.
* **Immutable Audit Ledger:** Every stock change (`RESTOCK`, `CUSTOMER_SALE`, `RETURN`, `ADJUSTMENT`) is recorded in an append-only `stock_movement` table with `UPDATE` and `DELETE` permissions revoked from the application role.
* **Idempotent Payment Processing:** Enforces `UNIQUE` gateway transaction references (`transaction_ref`) to prevent duplicate order fulfillment from webhook retries (supports Mobile Money, Cards, and Cash on Delivery).
* **Historical Price Integrity:** Locks `unit_price_at_purchase` inside `order_items` so future catalog price updates never alter past customer receipts.
* **Security & Privacy First:**
  * Uses `UUID` (`pgcrypto`) for customer IDs to prevent enumeration attacks.
  * Implements a least-privilege `inventory_app` role instead of exposing the `postgres` superuser.
* **Query Optimization:** Includes partial B-Tree indexes (`WHERE is_published = TRUE`) and foreign key indexes for fast storefront browsing and order lookups.

---

## Database Architecture (10 Core Tables)

| Domain | Table | Description |
| :--- | :--- | :--- |
| **Catalog** | `categories` | Product groupings with SEO-friendly URL `slug`s. |
| **Catalog** | `products` | Master catalog with `sku`, pricing (`NUMERIC(12,2)`), and publish status. |
| **Inventory** | `warehouses` | Physical store branches and storage locations. |
| **Inventory** | `inventory_level` | Real-time tracking of `on_hand` vs. `reserved` stock per warehouse. |
| **Inventory** | `stock_movement` | Append-only audit log of all inventory inflows and outflows. |
| **Customers** | `customer` | Buyer profiles using `UUID` primary keys and optional guest checkout. |
| **Customers** | `customer_address` | Multiple saved delivery addresses per customer. |
| **Commerce** | `orders` | Order lifecycle tracking (`PENDING_PAYMENT` → `DELIVERED`). |
| **Commerce** | `order_items` | Line items locking product quantity and price at checkout. |
| **Commerce** | `payments` | Payment provider tracking (`MTN_MOMO`, `ORANGE_MONEY`, Stripe, etc.). |

---

## Quick Setup

### Prerequisites
* PostgreSQL 14+
* `psql` CLI or pgAdmin 4

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com
   cd postgres-ecommerce-inventory
   ```

2. Update the `inventory_app` password inside `schema.sql`, then run the setup script via `psql`:
   ```bash
   psql -U postgres -f schema.sql
   ```

3. Connect your backend application using the restricted role:
   ```env
   DATABASE_URL=postgresql://inventory_app:your_secure_password@localhost:5432/inventory
   ```

---

## Checkout Concurrency Flow

To prevent race conditions when multiple customers buy the last item in stock simultaneously, execute checkout reservations inside an atomic transaction:

```sql
BEGIN;

SELECT quantity_on_hand, quantity_reserved
FROM inventory_level
WHERE product_id = \$1 AND warehouse_id = \$2
FOR UPDATE;

-- Verify (quantity_on_hand - quantity_reserved) >= requested_qty in backend
UPDATE inventory_level
SET quantity_reserved = quantity_reserved + \$3, updated_at = NOW()
WHERE product_id = \$1 AND warehouse_id = \$2;

COMMIT;
```

---

## License
MIT License
