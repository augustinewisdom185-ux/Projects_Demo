
# School Grade Management System Program (SGMSP)
---

A lightweight, terminal-based Python application designed to help educators manage student records, calculate averages, and assign grades.
The system runs entirely in the command line and uses an in-memory dictionary to store and retrieve student data efficiently using JSON formatting for readability.

---

## 🌟 Features
This program features a fully interactive menu that allows you to perform the following operations:
* **Add Students:** Input a student's name, age, subjects, and marks. The system automatically calculates their percentage average (based on a constant 1000-mark total per subject) and assigns a letter grade (A to F).
* **View All Students:** Displays the entire database of student records in a clean, human-readable JSON format.
* **Find the Top Student:** Automatically scans the database and identifies the student with the highest average.
* **Update Student Records:** Modify an existing student's data. You can update their age, add/modify subject marks (which automatically recalculates their total, average, and grade), or manually override their final letter grade.
* **Search for a Student:** Quickly retrieve a specific student's full profile by searching for their name.
* **Delete a Student:** Safely remove a student's record from the database with a built-in confirmation prompt to prevent accidental deletions.

---

## 📋 Prerequisites
This program uses only Python's standard libraries. There is no need to install external packages or dependencies.
* **Python 3.14.5** installed on your machine.

---

## 🚀 How to Run
1. Save the provided Python code into a file named `sgmsp.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the script using the following command:

```bash
python sgmsp.py

