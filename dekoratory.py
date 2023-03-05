#dekorator zaczyna sie od @
import datetime
def dodaj_date(func):
    def inner():
        teraz = datetime.datetime.now()
        print('Aktualnie mamy',teraz.strftime('%H:%M:%S'))
        print('Logowanie włączone')
        func()
    return inner

@dodaj_date
def przywitanie():
    print('hejka')

przywitanie()

def smart_divice(func):
    def inner(a, b):
        print('Bede dzielil')
        if b == 0:
            print('nie moge')
            return
        return func(a, b)
    return inner

@smart_divice
def divide(a, b):
    print(a/b)

def device(a, b):
    print(a/b)