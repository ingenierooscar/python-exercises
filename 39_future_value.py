amt = int(input("type amount: "))
inte = float(input("type int: "))
year = int(input("type year: "))


def calculate_rate(a, b, c):
    resu = 0
    resu = a*((1 + (0.01*b))**c)
    return resu


print(round(calculate_rate(amt, inte, year), 2))


future_value = amt*((1+(0.01*inte)) ** year)
print(round(future_value, 2))
