"""
Lori Walden, SDEV 220
Student Achievement Tracker App (M02Lab-Case_Study_if_else)

This app will accept the input of a student (their first and last name, and GPA) and 
will output if they qualify for either the Dean's List (GPA is 3.5 or greater) or 
the Honor Roll (GPA is 3.25 or greater). Entering "ZZZ" will exit the program.
"""

# Declare variables
deans_list_min = 3.5      # GPA threshold for Dean's List
honor_roll_min = 3.25     # GPA threshold for Honor Roll

# Intiialize Program
last_name = input("Please enter student's last name, or enter 'ZZZ' to quit: ")

# While Loop for Program
while last_name != "ZZZ":
    first_name = input("Please enter student's first name: ")
    GPA = float(input("Please enter student's GPA: "))

    if deans_list_min <= GPA:
        print(first_name, last_name, "made the Dean's List.")
    elif honor_roll_min <= GPA:
        print(first_name, last_name, "made the Honor Roll.")
    last_name = input("Please enter student's last name, or enter 'ZZZ' to quit: ")

# End of Program
print("Thank you for using the Student Achievement Tracker App.")
