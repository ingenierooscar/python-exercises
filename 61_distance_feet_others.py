feet = int(input("type feet: "))


def feet_to_others(feet):
    return print(f" inches {feet * 12}\n yards {feet / 3}\n miles {feet / 5280}")


feet_to_others(feet)
