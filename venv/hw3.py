toys = {"F" : [] , "M": []}
class Toy:
    def __init__(self, animal = None):
        self.animal = animal
        self.owners = []
    def add_owner(self, Dog):
        self.owners.append(Dog)
    def show_owners(self):
        if self.owners != 0 :
            print(f"{self.animal} is owned by:")
            for owner in self.owners:
                print(owner.nickname)
        else:
            print("First add owners for toys")
class Dog():
    def __init__(self, nickname):
        self.nickname = nickname
foofy = Dog("Foofy")
max= Dog("Max")
toy1 = Toy("elephant")
toy2 = Toy("lion")
toy1.add_owner(foofy)
toy1.add_owner(max)
toy2.add_owner(max)
toy2.show_owners()
toy1.show_owners()

