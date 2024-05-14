# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   M. Espinoza, 05/13/2024, Created the script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

# Defining functions
def quit_program():
    exit()

# Define the Data Constants
MENU: str = """
----Course Registration Program----
Select from the following menu: 
1. Register a Student for a Course
2. Show current data
3. Save data to a file
4. Exit the program
-------------------------------
"""
FILE_NAME: str = "Enrollments.csv"

# Defining Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file = None
menu_choice: str = ""
student_data: dict = {}
students: list = []

# Running while loop with error handling
try: 
    while True:
        print(MENU)
        menu_choice = input("Hello, please select from the options above: ")

        # Option 1: Registering a student for a course
        if menu_choice == "1": 
            # try: 
            student_first_name = input("Enter the student's first name: ")
            # except Exception as e:
            print("Error in first name!")
            # try: 
            student_last_name = input("Enter the student's last name: ") 
            # except Exception as e:
            print("Error in last name!")
            course_name = input("Enter the course the student is enrolling in: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"Thank you. {student_first_name} {student_last_name} has now been enrolled in {course_name}")
                    
        # Option 2: Displaying the registered students
        elif menu_choice == "2":
            for row in students:
                print(f'{row["FirstName"]},{row["LastName"]},{row["CourseName"]}')
            continue

        # Option 3: Saving file to csv
        elif menu_choice == "3":
            # try: 
            file = open(FILE_NAME, "w")
            for row in students:
                string_row = f'{row["FirstName"]},{row["LastName"]},{row["CourseName"]}\n'
                file.write(string_row)
            file.close()
            # except FileNotFoundError as e: 
            # print("ERROR! File not found!")
            continue    

                # Menu choice 4 - ending the program
        elif menu_choice == "4":
            print("You have ended the program.")
            quit_program()

        else: 
            print("Entry not valid. Please select option 1, 2, 3, or 4.")

except Exception as e:
    print("ERROR: There was an error while running the code!!")