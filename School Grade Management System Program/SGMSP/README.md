#School Grade Management System Program (SGMSP)
---

​A lightweight, terminal-based Python application designed to help educators manage student records, calculate averages, and assign grades.
​The system runs entirely in the command line and uses an in-memory dictionary to store and retrieve student data efficiently using JSON formatting for readability.

---

​##🌟 Features
​This program features a fully interactive menu that allows you to perform the following operations:
​Add Students: Input a student's name, age, subjects, and marks. The system automatically calculates their percentage average (based on a constant 1000-mark total) and assigns a letter grade (A to F).
​View All Students: Displays the entire database of student records in a clean, human-readable JSON format.
​Find the Top Student: Automatically scans the database and identifies the student with the highest average.
​Update Student Records: Modify an existing student's data. You can update their age, add/modify subject marks (which automatically recalculates their total, average, and grade), or manually override their final letter grade.
​Search for a Student: Quickly retrieve a specific student's full profile by searching for their name.
​Delete a Student: Safely remove a student's record from the database with a built-in confirmation prompt to prevent accidental deletions.

---

​##📋 Prerequisites
​This program uses only Python's standard libraries. There is no need to install external packages or dependencies.
​*Python 3.14.5 installed on your machine.

---
​##🚀 How to Run
​1. Save the provided Python code into a file named sgmsp.py (or whatever name you prefer).
​2. Open your terminal or command prompt.
​3. Navigate to the directory where you saved the file.
​4. Run the script using the following command:
``bash
python SGMSP.py

---

##💻 Usage Guide
​Once you run the script, you will be greeted with the main display menu:

========================================
             DISPLAY MENU             
========================================
1. Add students/Calculate average and grade.
2. View all students.
3. Top student in a class.
4. Update student's grade.
5. Search a student.
6. Delete a student.
7. Exit program.

---

Simply type the number corresponding to the action you want to take and press Enter.
​Important Notes on Data Entry:
​Case Insensitivity: The program automatically standardizes names and subjects using .title() to prevent duplicate entries caused by capitalization errors (e.g., "math" and "Math" are treated as the same subject).
​Exiting Loops: When adding students or subjects, you can type done at any time to finish the data entry process and return to the main menu.
​Grading Scale: The average percentage is calculated based on an assumed maximum total of 1000 marks across all subjects. The grading scale is:

​A: 80% - 100%
​B+: 70% - 79%
​B: 60% - 69%
​C: 50% - 59%
​D: 40% - 49%
​F: Below 40%

---

​##🛠️ Data Structure
​Under the hood, the program stores data in a nested Python dictionary. When viewing a student, the data structure looks like this:

{
    "Student Name": 
    {
        "Name": "Student Name",
        "Age": 18,
        "Subjects": {
            "Math": 850.0,
            "Science": 900.0
        },
        "Total Marks": 1750.0,
        "Average": 85.0,
        "Grade": "A"
    }
}
