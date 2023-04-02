numb1 = int(input("type number1: "))
numb2 = int(input("type number2: "))


def two_are_int(a, b):
    if type(a) and type(b) is int:
        return a + b
    else:
        return "must be integers!"


print(two_are_int("w", "d"))
