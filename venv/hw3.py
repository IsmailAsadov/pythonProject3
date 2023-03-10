class parts:
    B = []
    M = []
brand= "None"
class cars(brand):
    def __init__(self):
        self.brand = brand
bmw = cars("BMW")
mercedes = cars("Mercedes")
parts.B.append(input("What parts should we install in BMW:"))
parts.M.append(input("What parts should we install in mercedes:"))