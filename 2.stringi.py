nazwa = 'Kamil Adam Musial'
nazwa_ze_zmiana = nazwa.replace('i', '_DUZE_I_', 1)   #co, na co, ile razy
print(nazwa_ze_zmiana)

print(nazwa.replace(' ', ''))   #zamien spacje na nic
print(nazwa.replace(' ', '\n'))  #zamien spacje na enter

#nazwa_podzielona = nazwa.split()  #zamiana na listę po spacji

for slowo in nazwa.split():
    print(slowo)

