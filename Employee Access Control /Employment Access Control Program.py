import random
import string

# Funtion Definition.

def add_user_id(name, age, country):
    """Generates a unique ID and returns a formatted employee string."""
    characters = string.ascii_uppercase + string.digits
    # Generate a random 5-character ID
    emp_id = ''.join(random.choices(characters, k=5))
    #k = 5is for 5 stings of numbers if you wan more increse the value from 5 to infinty or below.
    # Default rank is 'Junior' and default status is 'Active'
    return f"{name} : {emp_id} : {age} : {country} : Junior : Active"

def scan_employee_id(search_id):
    """Checks if an ID exists and if the employee is active."""
    try:
        with open("Employee.txt", "r") as file:
            for line in file:
                parts = line.strip().split(" : ")
                if parts[0] == search_id:
                    if parts[5] == "Fired":
                        return "ACCESS DENIED: Employee has been fired."
                    return f"ACCESS GRANTED: Welcome {parts[1]} ({parts[4]})"
        return "ACCESS DENIED: ID not found."
    except FileNotFoundError:
        return "Error: Database file not found."

def update_employee(emp_id, action):
    """Promotes, Demotes, or Fires an employee by updating the file."""
    updated_data = []
    found = False
    
    try:
        with open("Employee.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            parts = line.strip().split(" : ")
            if parts[0] == emp_id:
                found = True
                if action == "Fire":
                    parts[5] = "Fired"
                elif action == "Promote":
                    parts[4] = "Senior"
                elif action == "Demote":
                    parts[4] = "Junior"
                updated_data.append(" : ".join(parts) + "\n")
            else:
                updated_data.append(line)

        if found:
            with open("Employee.txt", "w") as file:
                file.writelines(updated_data)
            print(f"Successfully performed '{action}' on ID: {emp_id}")
        else:
            print("Employee ID not found.")
            
    except FileNotFoundError:
        print("Error: No employee records found.")

# --- MAIN PROGRAM LOOP ---

while True:
    print("\n" + "="*10, "EMPLOYMENT ACCESS CONTROL Program (EACP)", "="*10)
    print("1. Add Employee")
    print("2. Scan Employee ID")
    print("3. Manage Employee (Promote/Demote/Fire)")
    print("4. Exit")
    
    choice = input("Enter option (1-4): ")

    if choice == '1':
        print("\n--- Adding New Employee ---")
        name = input("Enter name: ").strip().capitalize()
        age = input("Enter age: ")
        country = input("Enter country: ").strip().upper()
        
        entry = add_user_id(name, age, country)
        with open("Employee.txt", "a") as file:
            file.write(entry + "\n")
        print(f"Employee added! Generated ID: {entry.split(' : ')[0]}")

    elif choice == '2':
        search_id = input("Scan/Enter ID: ").strip().upper()
        print(scan_employee_id(search_id))

    elif choice == '3':
        emp_id = input("Enter Employee ID: ").strip().upper()
        print("Actions: Promote | Demote | Fire")
        action = input("Enter action: ").strip().capitalize()
        if action in ["Promote", "Demote", "Fire"]:
            update_employee(emp_id, action)
        else:
            print("Invalid action.")

    elif choice == '4':
        print("Exiting System...")
        break
    else:
        print("Invalid selection, please try again.")
