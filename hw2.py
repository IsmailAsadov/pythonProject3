class cat():
    def __init__(self, name = None):
        self.hunger = 50
        self.satisfaction = 100
        self.fur = 10
        self.health = 100
noar = cat("Noar")
day_num = 0
while True:
    decision = input("Continue? Y or N")
    if decision == "Y":
        day_num += 1
        print(f"It's day: {day_num}")
        noar.hunger -= 1
        noar.satisfaction -= 2
        noar.fur += 1
        noar.health -= 1
        if noar.hunger < 30:
            print("meow, give me food")
            noar.hunger.grow(30)
        if noar.satisfaction < 20:
            print("I want to play MEOOOWW")
            noar.satisfaction.grow(20)
        if noar.fur >30:
            print(f"{cat.name} has been too hairy lately")
        if noar.health < 60:
            print(f"you should take {cat.name} to the vet")
            ToVet = input(f"Do you want to take {cat.name} to the vet? Y or N")
            if ToVet != "Y":
                print("You are a bad owner!!!")
            else:
                noar.health.grow(20)
        if noar.health <= 0:
            print(f"OH NO {cat.name} died!")
            break
    elif decision == "N":
        pass
    else:
        print("stop cheating!!!")
