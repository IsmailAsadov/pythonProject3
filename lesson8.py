def adder(*args, **kwargs):
    result = 0
    for i in args:
        result += i
    for i in kwargs.values():
        result += i
    return result