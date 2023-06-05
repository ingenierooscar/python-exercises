weight = int(input("type weight: "))
height = float(input("type height: "))


def bode_max(x, y):
    body = 0
    body = x / (y**2)
    print(body)


bode_max(weight, height)
