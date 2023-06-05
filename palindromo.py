

def palindomo(pal):
    pal = pal.lower()
    pal = pal.replace(' ', '')
    texto_al = revertir(pal)
    return texto_al


def revertir(pal):
    texto_al_reves = ""
    for char in pal:
        texto_al_reves = char + texto_al_reves
        print(texto_al_reves)
    return texto_al_reves


# just to check modification date
print(palindomo("aeiou"))
