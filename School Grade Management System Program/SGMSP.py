import json

sgmsp = {}

print("================================================")
print("School Grade Management System Program(SGMSP)")
print("================================================\n")

# Display function
def display_menu():
    # Adding a loop so the menu keeps showing until the user exits
    while True:
        print("\n" + "="*40)
        print("             DISPLAY MENU             ")
        print("="*40)

        print("1. Add students/Calculate average and grade.")
        print("2. View all students.")
        print("3. Top student in a class.")
        print("4. Update student's grade.")
        print("5. Search a student.")
        print("6. Delete a student.")
        print("7. Exit program.")

        try:
            option = int(input("Enter option of operation: "))
            if option == 1:
                add_student()
            elif option == 2:
                view_std()
            elif option == 3: 
                top_student()
            elif option == 4:
                upgrade_values_keys()
            elif option == 5:
                search_student()
            elif option == 6:
                delete_student()
            elif option == 7:
                print("Exiting the program. Bye!")
                break # This breaks the loop and ends the program
            else:
                print("Invalid option. Please choose a number between 1 and 7.")
        except ValueError:
            print("Invalid input! Please enter a number, not text.")

# Add student function, Calculate average and Grade.
def add_student():
    print("\n==============================================")
    print("    ADD STUDENTS/CALCULATE AVERAGE AND GRADE    ")
    print("================================================")

    while True:
        raw_name = input("Enter name here (or 'done' to stop): ").strip()
        # Adjusted the break condition slightly to be more intuitive
        if raw_name.lower() == "done":
            break
            
        try:
            age = int(input(f"Enter age for {raw_name.title()}: "))
        except ValueError:
            print("Invalid age. Returning to menu.")
            break
            
        name = raw_name.title()
        student_profile = {}
        student_score = {}

        student_profile["Name"] = name
        student_profile["Age"] = age

        # Entering secondary loop
        print(f"---- Entering subjects for {name} ----")

        while True:
            raw_subject = input("Enter subject name (or 'done' to finish subjects): ").strip()
            if raw_subject.lower() == "done":
                break
                
            subject = raw_subject.title()
            
            try:
                marks = float(input(f"Enter marks for {subject}: "))
                student_score[subject] = marks
            except ValueError:
                print("Invalid marks entered. Please enter a number.")

        # After subjects are entered, calculate totals
        student_profile["Subjects"] = student_score
        total_marks = sum(student_score.values())
        student_profile["Total Marks"] = total_marks

        # Calculating average based on a constant total of 1000 marks
        if total_marks > 0:
            # Formula: (Student's Total / 1000) * 100 to get the percentage
            average = (total_marks / 1000) * 100
        else:
            average = 0.0
            
        student_profile["Average"] = average

        # Control flow for grading based on the calculated percentage
        if average >= 80:
            grade = 'A'
        elif average >= 70:
            grade = 'B+'
        elif average >= 60:
            grade = 'B'
        elif average >= 50:
            grade = 'C'
        elif average >= 40:
            grade = 'D'
        else:
            grade = 'F'
            
        student_profile["Grade"] = grade

        # FIXED: Use the student's actual name as the key, not "Name of students"
        sgmsp[name] = student_profile
        print(f"\nStudent {name} added successfully!")


def view_std()->str:
    print("\n==============================================")
    print("               VIEW ALL STUDENTS              ")
    print("================================================")
    if not sgmsp:
        print("No students in the database yet.")
    else:
        # dump here is used to unpack the data from the file to my terminal.
        # indent is used to make the code human readable.
        print(json.dumps(sgmsp, indent = 4))


def top_student()->str:
    print("\n==============================================")
    print("                 TOP STUDENT                  ")
    print("================================================")
    if sgmsp:
        top_std = max(sgmsp, key=lambda student: sgmsp[student]["Average"])
        highest_Av = sgmsp[top_std]["Average"]
        print(f"The highest average is {highest_Av:.2f}% scored by {top_std}")
    else:
        print("No student found.")


def upgrade_values_keys()->str:
    print("\n===================================")
    print("     UPDATE STUDENT RECORD MENU      ")
    print("=====================================")

    if not sgmsp:
        print("No student records found to be updated.")
        return
        
    student_name = input("Enter full student name: ").title().strip()
    if student_name not in sgmsp:
        print(f"'{student_name}' not found in the system.")
        return
    
    print(f"What would you want to update for {student_name}?")
    print("1. Update age.")
    print("2. Update/Add subject/marks")
    print("3. Manually update grade.")
    print("4. Return to main menu.")
    
    try:
        choice = int(input("Enter operation here: "))
        if choice == 1:
            try:
                new_age = int(input(f"Enter new age for {student_name}: "))
                sgmsp[student_name]["Age"] = new_age
                print(f"Successfully updated age to {new_age}!")
            except ValueError:
                print("Invalid input! Age must be a number.")
                
        elif choice == 2:
            subject = input("Enter the subject name: ").title().strip()
            try:
                new_mark = float(input(f"Enter new marks for {subject}: "))
                sgmsp[student_name]["Subjects"][subject] = new_mark
                print(f"Successfully updated {subject} to {new_mark}!")

                # Recalculate based on the new marks and the 1000 maximum scale
                all_scores = sgmsp[student_name]["Subjects"]
                total = sum(all_scores.values())
                avg = (total / 1000) * 100 

                sgmsp[student_name]["Total Marks"] = total
                sgmsp[student_name]["Average"] = avg

                if avg >= 80: sgmsp[student_name]["Grade"] = "A"
                elif avg >= 70: sgmsp[student_name]["Grade"] = "B+"
                elif avg >= 60: sgmsp[student_name]["Grade"] = "B"
                elif avg >= 50: sgmsp[student_name]["Grade"] = "C"
                elif avg >= 40: sgmsp[student_name]["Grade"] = "D"
                else: sgmsp[student_name]["Grade"]  = "F"

                print("Total marks, Average, and Grade have been updated successfully.")

            except ValueError:
                print("Invalid input! Marks must be a number.")

        elif choice == 3:
            current_grade = sgmsp[student_name]["Grade"]
            print(f"Current grade is: {current_grade}")
            new_grade = input("Enter new Grade: ").upper().strip()
            sgmsp[student_name]["Grade"] = new_grade
            print(f"Successfully upgrading the grade to: '{new_grade}'! ")
            
        elif choice == 4:
            print("Returning to main menu.")
        else:
            print("Invalid choice selection.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")


def search_student():
    print("\n=====================================")
    print("            SEARCH STUDENT           ")
    print("=====================================")

    if not sgmsp:
        print("The database is completely empty")
        return
        
    search_name = input("Enter name of the student to search here: ").strip().title()
    
    if search_name in sgmsp:
        print(f"Record for {search_name} found:")
        # json.dumps prints the inner dictionary with nice indentation
        print(json.dumps(sgmsp[search_name], indent = 4))
    else:
        print(f"No record found for a student named '{search_name}'.")


def delete_student()->str:
    print("\n===================================")
    print("        DELETE STUDENT STATUS         ")
    print("=====================================")

    if not sgmsp:
        print(f"The database is empty. Nothing to delete.")
        return
        
    student_name = input("Enter name of student to delete here: ").strip().title()
    if student_name in sgmsp:
        confirmation = input(f"Are you sure you want to delete '{student_name}'? (y/n): ").strip().lower()
        if confirmation == 'y':
            del sgmsp[student_name]
            print(f"Successfully deleted '{student_name}' from the system.")
        else: 
            print("Deleting cancelled.")
    else: 
        print(f"Cannot delete: '{student_name}' does not exist.")

# This ensures the script only runs if executed directly (not imported as a module)
if __name__ == "__main__":
    display_menu()
