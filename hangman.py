# TODO importy
from random import choice

from postava import hangman
from slovnik import nahodne_slovo

# TODO promenne
zivoty = 7
hra_bezi = True
slovo = choice(nahodne_slovo()).strip()
tajenka = [' _ '] * len(slovo)


while hra_bezi and zivoty != 0:
    # zobraz tajenku
    print(f'Tajenka: {"".join(tajenka)}')

    # TODO input
    hadani = input('Hadej pismeno/slovo: ')
    if hadani.isalpha() == False:
        print('Tohle neni pismeno :( radeji skoncim, nez napachas neco horsiho')
        exit()

    if hadani == slovo:
        hra_bezi = False

    elif hadani in slovo and len(hadani) == 1:
        for index, symbol in enumerate(slovo):
            if symbol == hadani:
                tajenka[index] = hadani
        print('Uhodl jsi spravne pismeno!')

        # pokud uzivatel uhodl vsechna pismena
        if ' _ ' not in tajenka:
            hra_bezi = False

    # pokud uzivatel neuhodl
    else:
        zivoty -=1
        print(hangman[str(zivoty)])
else:
    if hra_bezi == False:
        print(f'Vyhral/a jsi správně slovo {slovo}')
    else:
        print(f'Prohral/a jsi, tajenka byla {slovo}')




