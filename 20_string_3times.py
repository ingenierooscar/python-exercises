""""
char = input("string: ")


def cadena(x):
    if x.isdigit() == True:
        print(x)
    else:
        print(x * 3)


cadena(char)
"""

char = input("palabra: ")
numb1 = int(input("numero: "))


def cadena(chars, numbers):
    """ emula la cadena como print("python" * 3)

    Args:
        chars (_type_): string
        numbers (_type_): numero
    """
    reslutado = ""
    for x in range(numbers):
        reslutado += chars
    print(reslutado)


cadena(char, numb1)
