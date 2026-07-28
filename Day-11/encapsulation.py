class Student:
    def __init__(self):
        self.__marks = 90

    def display(self):
        print("Marks:", self.__marks)

student = Student()

student.display()