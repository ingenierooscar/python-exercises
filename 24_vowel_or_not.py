char = input("type the letter: ")

"""
def vowel_o_not(char2):
    if char2 == "a" or char2 == "e" or char2 == "o" or char2 == "i" or char2 == "u":
        print("is a vowel")
    else:
        print("is not a vowel")
"""

# this is an other way


def vowel_o_not(char):
    vowel = "aeiou"
    print(char in vowel)


vowel_o_not(char)
