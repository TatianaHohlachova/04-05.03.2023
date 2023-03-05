czlowiek1 = ['Kamil', 'Musial', 34, 'M', 2, 3400]
czlowiek2 = ['Maciej', 'Kowalski', 32, 'M', 1, 3100]

czlowiek2[4] = 3
print(czlowiek2)

def zwieksz_wyplate(wyplata, zwieksz):
    return wyplata + zwieksz

czlowiek1[5] = zwieksz_wyplate(czlowiek1[5], 500)
print(czlowiek1)