numder = input("type number: ")
print(numder)


def digit_num(number):
    output = map(int, number)
    digits = list(output)
    suma = sum(digits)
    print(suma)


digit_num(numder)
