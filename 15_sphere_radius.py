import math

radio = int(input("radio is: "))


def sphere_volume(radio):
    radio = (4/3) * (math.pi * (radio**3))
    return radio


vol = sphere_volume(radio)

print(f"volume of sphere is: {vol}")
