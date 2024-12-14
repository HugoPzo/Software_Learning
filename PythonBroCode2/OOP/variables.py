class Student:

    # Class variables
    class_year = 2024
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Number of student were created
        Student.num_students += 1


student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 24)
student3 = Student("Crab", 64)


print(Student.num_students)

