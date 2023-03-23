a1 = int(input("first number: "))
a2 = int(input("second number: "))
a3 = int(input("third number: "))


def suma(num1, num2, num3):
    sumass = num1 + num2 + num3
    if num1 == num2 == num3:
        sumass = sumass * 3
    return sumass


print(suma(a1, a2, a3))
