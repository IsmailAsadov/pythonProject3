# class Human:
#     height =170
# class Student(Human):
#     height = 180
# nick = Student()
# print(nick.height)
# class Gparent:
#     age = 60
#     height = 170
#     satiety = 50
# class parent(Gparent):
#     age= 40
#     height = 180
# class child (parent):
#     age= 10
class Hello_world:
    hello = "hello"
    _hello = "_hello"
    __hello = "__Hello"
    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self.__hello)
        print(self.__world)
hello = Hello_world()
hello.printer()
hi = Hi()
hi.hi_print()

