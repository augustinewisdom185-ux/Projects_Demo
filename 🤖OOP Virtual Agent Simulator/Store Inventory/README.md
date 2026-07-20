# OOP Store Inventory & Reporting System

A modular Object-Oriented Programming (OOP) terminal application in Python that tracks stock levels for an e-commerce platform. It handles both **Physical** and **Digital Goods**, automates product categorization tagging, computes customized logistics handling fees, and exports automated textual audits alongside a localized database backup.

---

## 🚀 Key Features

* **Advanced OOP Architecture**: Implements clean Object-Oriented design principles such as Abstraction, Inheritance, and Method Overriding.
* **Dual-Product System**: Differentiates tracking behaviors seamlessly between `PhysicalProduct` (storing weights/shelves) and `DigitalProduct` (storing URLs/file sizes).
* **Automated Product Tagging**: An internal rules engine evaluates product names instantly to assign categories (`Electronics`, `Furniture`, `Construction`, or `General`).
* **Tiered Dynamic Pricing**: Implements dynamic pricing structures calculated automatically from physical weight variables.
* **Persistent JSON Storage**: Syncs your in-memory catalog straight into a clean, structures `Inventory_Item.json` flat database upon exit.
* **Automated Directory Reports**: Utilizes Python's native `os` library to auto-build a `Store_Reports/` folder, outputting text audit files for both active financial evaluations and structural restock alerts.

---

## 🛠️ OOP Architecture Concepts Used

### 1. Abstraction
The core blueprint relies on an Abstract Base Class (ABC) named `InventoryItem`. This class utilizes the `@abstractmethod` decorator to enforce strict contracts, forcing child subclasses to compute their handling configurations independently.

### 2. Inheritance & Overriding
Specific child instances (`PhysicalProduct` and `DigitalProduct`) inherit shared variables like `price` and `quantity` from the parent blueprint while completely overriding individual functional behaviors:
* **Physical Products**: Injects an extra dynamic logic layer that computes a handling fee of `$0.50` per kilogram.
* **Digital Products**: Bypasses traditional logistic computations entirely, returning a flat handle charge of `$0.00`.

### 3. Encapsulation & Memory Structures
Data manipulation properties (like individual object mutations or computing automated `stock_value` multipliers) are encapsulated inside localized method blocks. The live tracking catalog is maintained in an optimized Python `dictionary` using unique product IDs as lookup keys.

---

## 📁 System Outputs & File Structure

When you interact with the software and safely exit, it generates the following file tree layout:

```text
├── StoreInventory.py       # Main Application Source Code
├── Inventory_Item.json       # JSON Document Database State
└── Store_Reports/            # Auto-Generated Report Output Directory
    ├── final_inventory.txt   # Total Net Worth & System Financial Valuation
    └── restock_alerts.txt    # Low Stock Audit Warnings (Inventory Count < 3)
```

---

## 💻 Installation & Usage

### Prerequisites
Make sure you have Python 3.14.5 installed on your local computer system. No external third-party dependencies or libraries are required to run this code.

### Running the App
1. Clone this repository to your computer machine or download the source files.
2. Open your terminal window inside the project file directory path.
3. Boot the console script using the following execution command line:

```bash
python StoreInventory.py
```

4. Follow the interactive terminal prompts to feed in your product catalog items. 
5. Type `q` or `quit` to gracefully exit the software tool, sync data pipelines, and output the generated local audit reports.

---

## 📋 Sample Terminal Interaction Preview

```text
--- Welcome to the OOP Store Inventory System ---

What type of product do you want to add? (1: Physical, 2: Digital, 'q': Quit): 1
Enter product name: laptop
Enter product stock quantity: 2
Enter weight in kg: 15
Enter store room storage shelf location: A-12
Added laptop successfully as PHYS-101. Unit Price: \$10.00

What type of product do you want to add? (1: Physical, 2: Digital, 'q': Quit): q
Exiting store controller interface. Goodbye!

💾 Data completely synced to base database file: 'Inventory_Item.json'
📊 Reports auto-generated in folder 'Store_Reports': restock_alerts.txt & final_inventory.txt
```
