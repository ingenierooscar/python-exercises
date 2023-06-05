""""
#pasan un entero y le entrega una lista
numb1 = int(input("type number: "))


def number_list(numb2):
    list_numb = []
    for x in range(numb2 + 1):
        list_numb.append(x)
    print(list_numb)


number_list(numb1)
"""

# Write a Python program to count the number 4 in a given list.


def count_four(numb2):
    resu = 0
    for n in numb2:
        if n == 4:
            resu += 1
    print(resu)


count_four([2, 4, 5, 4])
