class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course


def display_menu():
    print("MENU: ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")


def create_student():
    print("Enter the student details below: ")
    name = input("Enter the student name: ")
    student_id = int(input("Enter the student ID: "))
    course = input("Enter the course name: ")

    student = Student(name, student_id, course)
    # Here the student object has been created -> and soon as it was created python calls the __init__() constructor.
    # Inside that constructor -> python first goes to self, then it stores the user entered values in the respective attributes -> substitutes the values in place of the attributes -> those values are stored in the created object "student" in their respective order.
    return student  # returns the created object to the caller main()


def display_student_info(student_list):

    if len(student_list) == 0:
        print("Nothing to show in the list!")
        return
    # now we print the data: for which we first access the attribute with the object name to retrieve the value stored in that attribute.
    # Objects use dot notation (.) to access their attributes.
    # In the for loop the element student will represent the object, so that for printing the values stored in different objects we can use the same element insted of using the particular object name again and again.

    else:
        print("STUDENT RECORDS: ")
        print("=" * 40)
    # Loop through the list -> going to each object (student) in the list and printing the contents stored in one object, at a time in each iteration.
    for student in student_list:
        print(f"Name:  {student.name}")
        print(f"Student ID: {student.student_id}")
        print(f"Course: {student.course}")
        # In the 1st iteration the student variable refers to the first student object in the students list.
        # Similarly, in the 2nd iteration, the student variables refers to the 2nd student object in the list.
        print("=" * 40)


def update_student(student_list):
    student_id = int(input("Enter student ID to update: "))

    for student in student_list:
        if student.student_id == student_id:
            student.name = input("Enter new name: ")
            student.course = input("Enter new course: ")
            print("Student details updated successfully!")
            return

    print("Student not found!")


def delete_student(student_list):
    student_id = int(input("Enter the Student ID to delete that student's details: "))
    for student in student_list:
        if student.student_id == student_id:
            student_list.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")


def main():
    print("=" * 40)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("Manage student records efficiently using Python.")
    print()

    # Creating empty student list
    student_list = []

    # append objects to the list
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            student = create_student()  # the student object returned by the create_student() is stored in the student variable.
            # Now we append the student object to the student list as:
            student_list.append(student)
            print("Student details added successfully!")

        elif choice == "2":
            # calling the display_student_info() to display the values:
            display_student_info(student_list)

        elif choice == "3":
            update_student(student_list)
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
