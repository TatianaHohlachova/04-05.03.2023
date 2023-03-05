from funkcje2_kod import *
#https://docs.python.org/3/tutorial/errors.html
licznik = 0
while True:
    wyplata = input('Ile zarabiasz? ')
    try:
        wyplata = float(wyplata)
        break
    except ValueError:
        print('zle dane, jeszcze raz')
        licznik += 1
    if licznik == 3:
        print('wypłata 2000zł')
        wyplata = 2000
        break

while True:
    liczba_dzieci = input('Ile masz dzieci? ')
    try:
        liczba_dzieci = int(liczba_dzieci)
        break
    except ValueError:
        print('zle dane, jeszcze raz')

try:
    print('kasa na dziecko =',wyplata / liczba_dzieci)
except ZeroDivisionError:
    print('cała kasa dla ciebie')


