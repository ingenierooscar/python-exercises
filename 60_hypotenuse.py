import math

a = int(input("side A: "))
b = int(input("side B: "))


def hypotenuse(a, b):
    hypo = 0
    hypo = math.sqrt((a**2)+(b**2))
    return hypo


print(hypotenuse(a, b))
