numb1 = int(input("type number: "))


def num_between(numb1):
    if numb1 <= 100:
        return print("is les that 100")
    elif 100 < numb1 <= 1000:
        return print("it's between 100 to 1000")
    else:
        return print("is grather that 2000")


numb2 = num_between(numb1)

# if the number is close to 1000 or 2000
# return ((abs(1000 - n <= 100) or (2000 - n <= 100)))
