class mercedes:
    year = 2009
class bmw:
    color = 'blue'
class audi:
    interior = "Leather"
class tesla:
    autopilot = True
class available_cars(mercedes, bmw, audi, tesla):
    pass
ac = available_cars
print(ac.year)
print(ac.color)
print(ac.interior)
print(ac.autopilot)