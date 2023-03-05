import time

def welcome_basic():
    time.sleep(0.5)
    print('przygotowywanie obrazu systemu')
    time.sleep(0.5)
    print('sprawdzanie bledow w systemie')
    time.sleep(0.5)
    print('Siema')

def welcome_full(imie, wiek):
    if wiek >= 18:
        print('Dzien dobry',imie)
    else:
        print('Czesc',imie)

def stan_zdrowia(waga = 65, wzrost = 1.8):
    BMI = waga / (wzrost**2)
    if BMI > 35:
        return 1
    elif BMI > 28:
        return 2
    return 3

def input_to_number(input):
    try:
        input = int(input)
        return input
    except:
        try:
            input = float(input)
            return input
        except:
            return False
def can_be_int(number):
    try:
        number = int(number)
        return True
    except:
        return False



