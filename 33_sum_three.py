numb1 = int(input("first number: "))
numb2 = int(input("second number: "))
numb3 = int(input("third number: "))


def sum_three(a1, a2, a3):
    resu = 0
    if a1 == a2 or a1 == a3 or a2 == a3:
        return resu
    else:
        resu = a1 + a2 + a3
        return resu


print(sum_three(numb1, numb2, numb3))
