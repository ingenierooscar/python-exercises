numb1 = int(input("type number 1: "))
numb2 = int(input("type number 2: "))
numb3 = int(input("type number 3: "))


def max_number(x1, x2, x3):
    max_value = max(x1, x2, x3)
    min_value = min(x1, x2, x3)
    mid_value = (x1 + x2 + x3) - max_value - min_value

    return "the max numbes is " + str(max_value) + " mid value is " + str(mid_value) + " the min calue is " + str(min_value)


print(max_number(numb1, numb2, numb3))
