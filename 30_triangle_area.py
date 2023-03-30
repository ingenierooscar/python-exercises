base = int(input("type base: "))
height = int(input("type height: "))


def are_triangle(base, height):
    area = (base * height) / 2
    return area


print(f"the area is: {are_triangle(base, height)}")
