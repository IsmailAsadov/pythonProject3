def my_dec(input_def):
    def output_def():
        print("-----------------")
        input_def()
        print("-----------------")

    return output_def

@my_dec
def inside():
    print("Внутри всего!")

inside()