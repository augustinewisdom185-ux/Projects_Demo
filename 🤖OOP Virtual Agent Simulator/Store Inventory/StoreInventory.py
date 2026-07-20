import os
import json
from abc import ABC, abstractmethod

class InventoryItem(ABC):
    def __init__(self, item_id, name, price, quantity, tags="General"):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.tags = tags
        # Stock value is calculated automatically (Price * Quantity)
        self.stock_value = self.price * self.quantity

    @abstractmethod
    def calculate_handling_fee(self):
        """Forces child classes to calculate extra costs differently."""
        pass

    def to_dict(self):
        """Converts object data into a clean dictionary format for JSON."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "tags": self.tags,
            "stock_value": self.stock_value,
            "handling_fee": self.calculate_handling_fee()
        }

class PhysicalProduct(InventoryItem):
    def __init__(self, item_id, name, price, quantity, weight, shelf_location, tags="General"):
        super().__init__(item_id, name, price, quantity, tags)
        self.weight = weight
        self.shelf_location = shelf_location

    def calculate_handling_fee(self):
        # Physical items add $0.50 handling fee per kg
        return round(self.weight * 0.50, 2)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Physical",
            "weight": self.weight,
            "shelf_location": self.shelf_location
        })
        return data

class DigitalProduct(InventoryItem):
    def __init__(self, item_id, name, price, quantity, download_url, file_size_mb, tags="Digital"):
        super().__init__(item_id, name, price, quantity, tags)
        self.download_url = download_url
        self.file_size_mb = file_size_mb

    def calculate_handling_fee(self):
        # Digital items don't cost anything extra to handle or ship
        return 0.00

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Digital",
            "download_url": self.download_url,
            "file_size_mb": self.file_size_mb
        })
        return data

class InventoryManager:
    def __init__(self):
        # 3. DICTIONARY DATABASE (Active Store Memory Store)
        self.database = {}
        self.report_folder = "Store_Reports"

        # Automatically make the reports folder if it doesn't exist
        if not os.path.exists(self.report_folder):
            os.makedirs(self.report_folder)

    def add_item(self, item_object):
        """Adds a built item instance into our active dictionary database."""
        self.database[item_object.item_id] = item_object

    def save_to_json(self, filename="Inventory_Item.json"):
        """Saves current database list cleanly into a new JSON file format."""
        clean_export = {"Items": [item.to_dict() for item in self.database.values()]}
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(clean_export, file, indent=4, ensure_ascii=False)
        print(f"\n💾 Data completely synced to base database file: '{filename}'")

    def generate_reports(self):
        """Creates alert logs and overall value summaries inside the directory."""
        alert_path = os.path.join(self.report_folder, "restock_alerts.txt")
        report_path = os.path.join(self.report_folder, "final_inventory.txt")

        # 1. Process Restock Alerts (Items dropping below 3 units)
        with open(alert_path, "w", encoding="utf-8") as alert_file:
            alert_file.write("=== RESTOCK ALERTS (STOCK RUNNING LOW) ===\n")
            for item in self.database.values():
                if item.quantity < 3:
                    alert_file.write(f"⚠️ ID: {item.item_id} | Name: {item.name} | Current Stock: {item.quantity}\n")

        # 2. Process Final Monetary Inventory Summary Report
        total_store_value = sum(item.stock_value for item in self.database.values())
        with open(report_path, "w", encoding="utf-8") as report_file:
            report_file.write("=== FINAL INVENTORY REPORT BALANCE ===\n")
            for item in self.database.values():
                report_file.write(
                    f"Product: {item.name} ({item.tags}) -> Quantity: {item.quantity} | Total Value: ${item.stock_value:.2f}\n")
            report_file.write("----------------------------------------\n")
            report_file.write(f"TOTAL RUNNING ACCOUNT NET WORTH: ${total_store_value:.2f}\n")

        print(f"📊 Reports auto-generated in folder '{self.report_folder}': restock_alerts.txt & final_inventory.txt")

def run_store_program():
    manager = InventoryManager()

    # Product category lookups
    electronics = ['phone', 'ear-pod', 'earpiece', 'laptop', 'charger', 'bulb']
    furniture = ['chair', 'table', 'dinning table', 'bed']
    construction = ['cement', 'blocks', 'rods', 'cutters']

    print("--- Welcome to the OOP Store Inventory System ---")
    id_counter = 101

    while True:
        choice = input("\nWhat type of product do you want to add? (1: Physical, 2: Digital, 'q': Quit): ").strip()
        if choice.lower() in ['q', 'quit']:
            print("Exiting store controller interface. Goodbye!")
            break

        if choice not in ['1', '2']:
            print("Invalid input option. Choose 1, 2, or q.")
            continue

        name = input("Enter product name: ").strip().lower()
        try:
            quantity = int(input("Enter product stock quantity: "))
        except ValueError:
            print("Invalid quantity number skipped.")
            continue

        # Automated Category Tagging Engine
        if name in electronics:
            tag = "Electronics"
        elif name in furniture:
            tag = "Furniture"
        elif name in construction:
            tag = "Construction"
        else:
            tag = "General"

        # --- Branch 1: Collect Physical Weights and Calculate Tier Pricing ---
        if choice == '1':
            try:
                weight = float(input("Enter weight in kg: "))
            except ValueError:
                print("Invalid numerical weight input.")
                continue

            # Weight calculation formulas
            if weight == 0:
                price = 0.0
            elif 1 <= weight <= 100:
                price = (weight / 3) * 2
            elif 0 < weight < 1:
                price = 5.00  # Added placeholder default fallback price for light weight
            else:
                print("Weight exceeds 100kg limit capacity.")
                continue

            shelf = input("Enter store room storage shelf location: ").strip()
            item_id = f"PHYS-{id_counter}"

            # Instantiation of the Physical Object
            product_instance = PhysicalProduct(item_id, name, price, quantity, weight, shelf, tag)
            manager.add_item(product_instance)
            id_counter += 1
            print(f"Added {name} successfully as {item_id}. Unit Price: ${price:.2f}")

        # --- Branch 2: Collect Digital Parameters ---
        elif choice == '2':
            try:
                price = float(input("Enter download price $: "))
                size = float(input("Enter download payload size (MB): "))
            except ValueError:
                print("Invalid input values.")
                continue

            url = input("Enter digital retrieval download URL link: ").strip()
            item_id = f"DIGI-{id_counter}"

            # Instantiation of the Digital Object
            product_instance = DigitalProduct(item_id, name, price, quantity, url, size, "Digital")
            manager.add_item(product_instance)
            id_counter += 1
            print(f"Added {name} successfully as {item_id}.")

    # Save tracking content state when quitting out
    if manager.database:
        manager.save_to_json()
        manager.generate_reports()

if __name__ == "__main__":
    run_store_program()
