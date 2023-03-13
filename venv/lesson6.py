try:
    print("start code")
    print(error)
    print("no errors")
except SyntaxError:
    print("Wrong syntax")
else:
    print("Aren't any errors")
finally:
    print("final code")
