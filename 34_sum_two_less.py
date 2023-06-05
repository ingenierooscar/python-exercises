numb1 = int(input("first number: "))
numb2 = int(input("second number: "))


def sum_two(a, b):
    resu = a + b
    if 15 <= resu <= 20:
        return 20
    else:
        return a + b


print(sum_two(numb1, numb2))
