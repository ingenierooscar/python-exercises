numb1 = int(input("enter number: "))


def diff_number(numb1):
    numb1 = numb1 - 17
    return abs(numb1)


numb2 = diff_number(numb1)
print(f"absolute value after difference of 17 is {numb2}")
