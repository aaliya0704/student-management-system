class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course


def main():
    print("=" * 40)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("Manage student records efficiently using Python.")
    print()

    # creating a new object named student_1
    student_1 = Student("Aaliya", 101, "Information Technology")
    student_2 = Student("Ali", 102, "BBA")
    # As soon as python sees that an object is to be created -> it calls the __init__ constructor.
    # In that constructor -> python first goes to self, then it stores the values in the respective attributes.

    # Creating empty student list
    student_list = []

    # append objects to the list

    student_list.append(student_1)
    student_list.append(student_2)

    # now we print the data: for which we first access the attribute with the object name to retrieve the value stored in that attribute.
    # Objects use dot notation (.) to access their attributes.
    # instead of manually writing print statement for each and every object we do this:
    # Loop through the list -> going to each object in the list and printing one at a time in each iteration
    for student in student_list:
        print(student.name)
    # In the 1st iteration the student variable refers to the first student object in the students list.
    # Similarly, in the 2nd iteration, the student variables refers to the 2nd student object in the list.


if __name__ == "__main__":
    main()
