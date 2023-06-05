numb1 = int(input("type number1: "))
numb2 = int(input("type number2: "))


def equal_sum_diff_five(a, b):
    if a == b or abs(a - b == 5) or a + b == 5:
        return True
    else:
        return False


print(equal_sum_diff_five(numb1, numb2))
