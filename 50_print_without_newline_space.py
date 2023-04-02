char = input("type test: ")


def without_newline_space(char):
    char = char.replace(" ", "")
    return char


print(without_newline_space(char))

for i in range(0, 10):
    # with end="" delete new line
    print('*', end="")
print("\n")
