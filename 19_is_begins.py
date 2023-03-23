word = input("type the word: ")


def already_begins_is(char):
    if char[:2] == "Is":
        return print(char)
    print("Is" + char)


already_begins_is(word)
