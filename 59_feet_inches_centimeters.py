feet = int(input("enter feet: "))
inches = int(input("enter inches: "))


def inches_to_cm(inches):
    if inches > 0:
        return inches / 0.39370
    else:
        return False


def feet_to_cm(feet):
    if feet > 0:
        return feet / 0.032808
    else:
        return False


print(feet_to_cm(feet))
print(inches_to_cm(inches))
print(inches_to_cm(inches)+feet_to_cm(feet))
