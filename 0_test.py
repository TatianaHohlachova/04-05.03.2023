napis = 'Kamil ma psa'
lista_zwierzat = ['pies', 'drugi pies', 'tu tez pies']

print(napis[2:6])
print(lista_zwierzat[2])
print(lista_zwierzat[2][3:7])
print(lista_zwierzat[2][-3])
for i in range(20, 4, -3):   #od, do, krok
    print(i)

for i in range(4):    #i jest iteratorem, można go użyć tak, jak chcemy
    print('okrazenie ',i+1,', a litera nr ',i+4,'to',napis[i+3],'\n')

for litera in napis:    #pętla po stringu (napis)
    print(litera)
for zwierze in lista_zwierzat:   #pętla po liście
    print(zwierze)

