#program, który sprawdzi, czy dane słowo to palindrom

slowo = input('Wpisz slowo ')
# liczba_iteracji = len(slowo)//2
# for i in range(liczba_iteracji):
#     if slowo[i] != slowo[-1 -i]:

if slowo == slowo[::-1]:
#https://www.w3schools.com/python/python_howto_reverse_string.asp
    print('Tak, palindrom')
else:
    print('Nie, nie palindrom')