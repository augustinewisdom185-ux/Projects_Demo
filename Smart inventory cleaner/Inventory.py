import json
from json import JSONDecodeError

raw_inventory = 'raw_inventory.json'

def display_inventory():
    current_inventory = None
    while True:
        print("\n1. Load Inventory.")
        print("2. Clean Inventory.")
        print("3. Changing Value.")
        print("4. Saving Data.")
        print("5. Exit Program.\n")

        try:
            option = int(input("Enter option(1-5): "))
            if option == 1:
                current_inventory = load_inventory()
            elif option == 2:
                current_inventory =  cleaning_inventory(current_inventory)
            elif option == 3:
                current_inventory = changing_value(current_inventory)
            elif option == 4:
                current_inventory = save_to_file(current_inventory)
            elif option == 5:
                print("Exiting...\nBye👋...")
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid option.\nEnter from (1-5)")
        except NameError as error:
            print(f"Name Tracking error!: {error}")
            return None

def load_inventory():
    try:
        with open(raw_inventory, encoding = 'utf-8') as file:
            inventory = json.load(file)
            for item in inventory['items']:
                print('\n','='*6,'Loading inventory...','='*6)
                for key,value in item.items():
                    print(f'{key}: {value}')
            return inventory
    except FileNotFoundError:
        print(f"File {raw_inventory} not found.")
        return None
    except TypeError as error:
        print(f"Error: {error}")
    except JSONDecodeError as error:
        print("Syntax error in your json decoder engine!.")
        print(f"Script failed because of: {error.msg}")
        print(f"To fix this check line: {error.lineno}")
        return inventory
    finally:
        print("\nLoading Inventory Completed!...")

#Accessing JSON file for cleaning and changing negative values
def cleaning_inventory(inventory):
    if not inventory or 'items' not in inventory:
        print("\nInventory is empty.")
        return inventory
    required_keys = ['product_id', 'stock', 'title', 'price', 'tags']

    try:
        for item in inventory['items']:
            print('\n','*'*6,'Cleaning inventory...','*'*6)
            if 'Price' in item:
                item['price'] = item.pop('Price')
                #del item['Price']
            if 'title' not in item:
                item['title'] = 'Unknown Product'
            if 'tags' not in item:
                item['tags'] = []
            for key in required_keys:
                if key in item:
                    print(f"{key}: {item[key]}")
        print("\n Renaming and filling blank spaces completed...")
        return inventory
#Except helps to prevent code from crashing.
    except RuntimeError as error:
        print("Dictionary can not be manipulated when looping..")
        print(f"Error: {error}")
        return inventory
    except TypeError as error:
        print("Dictionary can not be called..")
        print(f"Reason: {error}")
        return inventory

#Changing negative values in raw_inventory.
def changing_value(inventory):
    if not inventory or 'items' not in inventory:
        print("\nInventory is empty.")
        return inventory
    try:
        for item in inventory['items']:
            if 'stock' in item:
                if item['stock'] < 0:
                    item['stock'] = 0
                    print(f"Stock for product: {item.get('product_id')} : {item.get('stock')}")
        for item in inventory['items']:
            print('\n','_'*6, "New Record...",'_'*6)
            for key,value in item.items():
                print(f'{key}: {value}')
        print("\nStock adjustment completed...")
        return inventory

    except TypeError as error:
        print(f"Variable is completely empty")
        print(f"Error: {error}")
    finally:
        print("Changing Value Completed!")

#Saving to file called Cleaned_inventory
def save_to_file(inventory):
    if not inventory or 'items' not in inventory:
        print("\nInventory is empty.")
        return inventory
    saved_file = 'Cleaned Inventory.json'
    try:
        with open(saved_file, 'w', encoding = 'utf-8') as file:
            json.dump(inventory, file, indent =4, ensure_ascii = False)
            print(f"\nData Successfully Saved to {saved_file}")
    except Exception as error:
        print(f"Failed to save data because of: {error}")
display_inventory()
