class my_student:
    print("Hi!")
    def __init__(self):
        self.height = 174
        print("i'm alive?")
student = my_student()
class Student:
    def __init__(self):
        self.height = 174
        self.weight = 53
        self.hair = 'brown'
Ismail = Student()
print(Ismail.height)
class Student:
    amount_of_s = 0
    def __init__(self, height = 174):
        self.height = height
        Student.amount_of_s += 1
Ismail = Student()
Kate = Student(height = 165)
print(Ismail.amount_of_s)
print(Student.amount_of_s)
class student:
    height = 160
    def __init__(self):
        print(self.height)
        self.height +=10

nick = student()
kate = student()
class Student:
    def __init__(self):
        self.height = 170
    height = 160
    def printer(self):
        print(self.height)
nick = Student()
nick.printer()