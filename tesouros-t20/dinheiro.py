from random import randint
from time import sleep
from riqueza import *

def dinheirorep0():
    sleep(0.4)
    print('Sua rolagem de dinheiro não rendeu nada.')

def dinheirorep1():
    d1 = randint(1, 4)
    dfinal = f'{d1 * 100} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou {d1} x 100 T$')
    return dfinal

def dinheirorep2():
    d1 = randint(1, 12)
    d2 = randint(1, 12)
    d3 = randint(1, 12)
    d4 = randint(1, 12)
    dfinal = f'{(d1 + d2 + d3 + d4) * 10} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2} + {d3} + {d4}) x 10 T$')
    return dfinal

def dinheirorep3():
    d1 = randint(1, 10)
    d2 = randint(1, 10)
    dfinal = f'{(d1 + d2) * 100} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2}) x 100 T$')
    return dfinal

def dinheirorep4():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)
    d4 = randint(1, 6)
    dfinal = f'{(d1 + d2 + d3 + d4) * 100} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2} + {d3} + {d4}) x 100 T$')
    return dfinal

def dinheirorep5():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)
    dfinal = f'{(d1 + d2 + d3) * 1000} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2} + {d3}) x 1000 T$')
    return dfinal

def dinheirorep6():
    d1 = randint(1, 4)
    d2 = randint(1, 4)
    dfinal = f'{(d1 + d2) * 1000} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2}) x 1000 TO')
    return dfinal


def dinheirondquarto(rolldinheiro):
    if rolldinheiro < 30:
        dinheirorep0()
        return 0
    elif rolldinheiro < 70:
        d1 = randint(1, 6)
        dfinal = f'{d1 * 10} TC'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} x 10 TC')
        return dfinal
    elif rolldinheiro < 95:
        d1 = randint(1, 4)
        dfinal = f'{d1 * 100} TC'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} x 100 TC')
        return dfinal
    else:
        d1 = randint(1, 6)
        dfinal = f'{d1 * 10} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} x 10 T$')
        return dfinal

def dinheirondmeio(rolldinheiro):
    if rolldinheiro < 25:
        dinheirorep0()
        return 0
    elif rolldinheiro < 70:
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        dfinal = f'{(d1 + d2) * 10} TC'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2}) x 10 TC')
        return dfinal
    elif rolldinheiro < 95:
        d1 = randint(1, 8)
        d2 = randint(1, 8)
        dfinal = f'{(d1 + d2) * 10} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2}) x 10 T$')
        return dfinal
    else:
        dfinal = dinheirorep1()
        return dfinal

def dinheirond1(rolldinheiro):
    if rolldinheiro < 20:
        dinheirorep0()
        return 0
    elif rolldinheiro < 70:
        d1 = randint(1, 8)
        d2 = randint(1, 8)
        d3 = randint(1, 8)
        dfinal = f'{(d1 + d2 + d3) * 10} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2} + {d3}) x 10 T$')
        return dfinal
    elif rolldinheiro < 95:
        dfinal = dinheirorep2()
        return dfinal
    else:
        d1 = riquezamenor(0)
        sleep(0.4)
        print(f'A sua riqueza total encontrada foi {d1}')
        return d1

def dinheirond2(rolldinheiro):
    if rolldinheiro < 15:
        dinheirorep0()
        return 0
    elif rolldinheiro < 55:
        d1 = randint(1, 10)
        d2 = randint(1, 10)
        d3 = randint(1, 10)
        dfinal = f'{(d1 + d2 + d3) * 10} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2} + {d3}) x 10 T$')
        return dfinal
    elif rolldinheiro < 85:
        d1 = randint(1, 4)
        d2 = randint(1, 4)
        dfinal = f'{(d1 + d2) * 100} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2}) x 100 T$')
        return dfinal
    elif rolldinheiro < 95:
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        dfinal = f'{(d1 + d2 + 1) * 100} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2} + 1) x 100 T$')
        return dfinal
    else:
        d1 = riquezamenor(0)
        sleep(0.4)
        print(f'A sua riqueza total encontrada foi {d1}')
        return d1
    
def dinheirond3(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 20:
        dfinal = dinheirorep2()
        return dfinal
    elif rolldinheiro < 60:
        dfinal = dinheirorep1()
        return dfinal
    elif rolldinheiro < 90:
        d1 = randint(1, 8)
        dfinal = f'{d1 * 10} TO'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} x 10 TO')
        return dfinal
    else:
        dfinal = 0
        dric = randint(1, 3)
        sleep(0.4)
        print(f'Você encontrou {dric} riquezas menores.')
        for c in range(0, dric):
            d = riquezamenor(0)
            sleep(0.4)
            print(f'Totalizando {d}')
            d = d[:-3]
            sleep(0.4)
            dfinal += int(d)
        dfinal = f'{dfinal} T$'
        print(f'A sua riqueza total encontrada foi {dfinal}')
        return dfinal

def dinheirond4(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 50:
        d1 = randint(1, 6)
        dfinal = f'{d1 * 100} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} x 100 T$')
        return dfinal
    elif rolldinheiro < 80:
        d1 = randint(1, 12)
        dfinal = f'{d1 * 100} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} x 100 T$')
        return dfinal
    elif rolldinheiro < 90:
        d1 = riquezamenor(20)
        sleep(0.4)
        print(f'A sua riqueza total encontrada foi {d1}')
        return d1
    else:
        dfinal = 0
        dric = randint(1, 3)
        sleep(0.4)
        print(f'Você encontrou {dric} riquezas menores.')
        for c in range(0, dric):
            d = riquezamenor(20)
            sleep(0.4)
            print(f'Totalizando {d}')
            d = d[:-3]
            sleep(0.4)
            dfinal += int(d)
        dfinal = f'{dfinal} T$'
        print(f'A sua riqueza total encontrada foi {dfinal}')
        return dfinal

def dinheirond5(rolldinheiro):
    if rolldinheiro < 15:
        dinheirorep0()
        return 0
    elif rolldinheiro < 65:
        d1 = randint(1, 8)
        dfinal = f'{d1 * 100} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} x 100 T$')
        return dfinal
    elif rolldinheiro < 95:
        d1 = randint(1, 4)
        d2 = randint(1, 4)
        d3 = randint(1, 4)
        dfinal = f'{(d1 + d2 + d3) * 10} TO'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2} + {d3}) x 10 TO')
        return dfinal
    else:
        d1 = riquezamedia(0)
        sleep(0.4)
        print(f'A sua riqueza total encontrada foi {d1}')
        return d1

def dinheirond6(rolldinheiro):
    if rolldinheiro < 15:
        dinheirorep0()
        return 0
    elif rolldinheiro < 60:
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        dfinal = f'{(d1 + d2) * 100} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2}) x 100 T$')
        return dfinal
    elif rolldinheiro < 90:
        dfinal = dinheirorep3()
        return dfinal
    else:
        dfinal = 0
        dric = randint(1, 3)
        sleep(0.4)
        print(f'Você encontrou {dric + 1} riquezas menores.')
        for c in range(0, dric + 1):
            d = riquezamenor(0)
            sleep(0.4)
            print(f'Totalizando {d}')
            d = d[:-3]
            sleep(0.4)
            dfinal += int(d)
        dfinal = f'{dfinal} T$'
        print(f'A sua riqueza total encontrada foi {dfinal}')
        return dfinal
    
def dinheirond7(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 60:
        d1 = randint(1, 8)
        d2 = randint(1, 8)
        dfinal = f'{(d1 + d2) * 100} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2}) x 100 T$')
        return dfinal
    elif rolldinheiro < 90:
        d1 = randint(1, 12)
        d2 = randint(1, 12)
        dfinal = f'{(d1 + d2) * 10} TO'
        sleep(0.4)
        print(f'O seu dinheiro rolou ({d1} + {d2}) x 10 TO')
        return dfinal
    else:
        dfinal = 0
        dric = randint(1, 4)
        sleep(0.4)
        print(f'Você encontrou {dric + 1} riquezas menores.')
        for c in range(0, dric + 1):
            d = riquezamenor(0)
            sleep(0.4)
            print(f'Totalizando {d}')
            d = d[:-3]
            sleep(0.4)
            dfinal += int(d)
        dfinal = f'{dfinal} T$'
        print(f'A sua riqueza total encontrada foi {dfinal}')
        return dfinal
    
def dinheirond8(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 55:
        dfinal = dinheirorep3()
        return dfinal
    elif rolldinheiro < 95:
        dfinal = 0
        dric = randint(1, 4)
        sleep(0.4)
        print(f'Você encontrou {dric + 1} riquezas menores.')
        for c in range(0, dric + 1):
            d = riquezamenor(0)
            sleep(0.4)
            print(f'Totalizando {d}')
            d = d[:-3]
            sleep(0.4)
            dfinal += int(d)
        dfinal = f'{dfinal} T$'
        print(f'A sua riqueza total encontrada foi {dfinal}')
        return dfinal
    else:
        d1 = riquezamedia(20)
        sleep(0.4)
        print(f'A sua riqueza total encontrada foi {d1}')
        return d1

def dinheirond9(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 35:
        d1 = riquezamedia(0)
        sleep(0.4)
        print(f'A sua riqueza total encontrada foi {d1}')
        return d1
    elif rolldinheiro < 85:
        dfinal = dinheirorep4()
        return dfinal
    else:
        dfinal = 0
        dric = randint(1, 3)
        sleep(0.4)
        print(f'Você encontrou {dric} riquezas médias.')
        for c in range(0, dric):
            d = riquezamedia(0)
            sleep(0.4)
            print(f'Totalizando {d}')
            d = d[:-3]
            sleep(0.4)
            dfinal += int(d)
        dfinal = f'{dfinal} T$'
        print(f'A sua riqueza total encontrada foi {dfinal}')
        return dfinal
