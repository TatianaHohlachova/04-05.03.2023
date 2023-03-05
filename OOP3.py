class Audi:
    def __init__(self, barwa, info_wprowadzone):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = info_wprowadzone
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
    def __str__(self):
        napis = (f'Audi ma kolor {self.kolor} i jest w kondycji {self.kondycja}')
        return napis
    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100
        return round(zasieg * 0.9)
    def ustaw_tryb(self, tryb):
#        self.tryb = tryb
        if tryb == 'eco':
            self.spalanie_na_100 = 10
            self.tryb_ekonomiczny = True
            print('Tryb eco')
        elif tryb == 'normal':
            self.spalanie_na_100 = 14
            self.tryb_ekonomiczny = False
            print('Tryb normal')
        else:
            print('tryb nierozpoznany, brak zmian')

    def wlacz_eco(self):
        self.spalanie_na_100 = 10
        self.tryb_ekonomiczny = True
        print('Tryb eco włączony')

    def wlacz_normal(self):
        self.spalanie_na_100 = 14
        self.tryb_ekonomiczny = False
        print('Tryb normal włączony')

moje_auto = Audi('czerwony', 4)
auto_sasiada = Audi('zielony', 5)
print(auto_sasiada.kondycja)
print(moje_auto)
print(moje_auto.zasieg())
moje_auto.ustaw_tryb('eco')
print(moje_auto.zasieg())