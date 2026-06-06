# Employment Access Control Program (EACP) 🏢

A lightweight, Python-based Command Line Interface (CLI) application built to manage employee access and administrative records. This script allows users to generate employee IDs, store records in a local text database, scan IDs for access clearance, and manage employee statuses dynamically.

## 🚀 Features

* **Add Employees:** Automatically generates a unique, randomized 5-character alphanumeric ID for new hires and saves their profile (Name, Age, Country).
* **Access Scanner:** Simulates an ID scanner. Grants access to active employees while denying access to unrecognized or "Fired" IDs.
* **Employee Management:** Admins can easily update an employee's file to **Promote** (Senior), **Demote** (Junior), or **Fire** them, which immediately impacts their access privileges.
* **Persistent Storage:** Utilizes local `.txt` file handling to store and rewrite database records, meaning data persists between sessions.

## 🛠️ Built With

* **Python 3.x**
* Standard Libraries: `random`, `string`

## 💻 How to Run

1. Clone this repository or download the `.py` script.
2. Ensure you have Python installed on your machine.
3. Run the script in your terminal:
   ```bash
   python eacp.py
