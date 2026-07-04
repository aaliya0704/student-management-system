class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course


def display_student_info(student_list):

    if len(student_list) == 0:
        print("Nothing to show in the list!")
        return
    # now we print the data: for which we first access the attribute with the object name to retrieve the value stored in that attribute.
    # Objects use dot notation (.) to access their attributes.
    # In the for loop the element student will represent the object, so that for printing the values stored in different objects we can use the same element insted of using the particular object name again and again.
    # Loop through the list -> going to each object (student) in the list and printing the contents stored in one object, at a time in each iteration.
    for student in student_list:
        print("Name: ", student.name)
        print("Student ID: ", student.student_id)
        print("Course: ", student.course)
    # In the 1st iteration the student variable refers to the first student object in the students list.
    # Similarly, in the 2nd iteration, the student variables refers to the 2nd student object in the list.


def display_menu():
    print("MENU: ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")


def main():
    print("=" * 40)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("Manage student records efficiently using Python.")
    print()

    # As soon as python sees that an object is to be created -> it calls the __init__ constructor.
    # In that constructor -> python first goes to self, then it stores the values in the respective attributes.

    # Creating empty student list
    student_list = []

    # append objects to the list
    while True:
        display_menu()

        choice = input("Enter your choice: ")
        if choice == "1":
            print()
        elif choice == "2":
            # calling the display_student_info() to display the values:
            display_student_info(student_list)
            print()
        elif choice == "3":
            print()
        elif choice == "4":
            print()
        elif choice == "5":
            print()
        elif choice == "6":
            print("Thank you for using the student management app!")
            break

        else:
            print("Invalid Choice. Make the choice between 1 - 6")


if __name__ == "__main__":
    main()
