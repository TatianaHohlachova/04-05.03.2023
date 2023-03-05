def high_salary(*args):
    print(args[0])     # wyświetlenie pierwszego argumentu
    print(args[1])         #wyświetlenie ostatniego argumentu
    print(len(args))
    for i in args:
        if i > 1000:
            print(f'Zarabia za duzo, bo, az {i}')

def welcome(**kwargs):
    if 'imie' in kwargs and 'nazwisko' in kwargs:
        print('Welcome',kwargs['imie'],kwargs['nazwisko'])
    elif 'imie' in kwargs:
        print('Hello ',kwargs['imie'])



high_salary(800, 900, 1000, 1100, 1200, 2100)
welcome(imie='Kamil', nazwisko='Kowalski', wiek=24)