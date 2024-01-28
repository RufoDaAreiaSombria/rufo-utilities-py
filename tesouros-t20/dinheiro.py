from random import randint
from time import sleep

def dinheirorep0():
    sleep(0.4)
    print('Sua rolagem de dinheiro não rendeu nada.')

def dinheirorep1():
    d1 = randint(1, 4)
    dfinal = f'{d1 * 100} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou {d1} * 100 T$')
    return dfinal

def dinheirorep2():
    d1 = randint(1, 12)
    d2 = randint(1, 12)
    d3 = randint(1, 12)
    d4 = randint(1, 12)
    dfinal = (d1 + d2 + d3 + d4) * 10
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2} + {d3} + {d4}) * 10 T$')
    return dfinal

def dinheirorep3():
    d1 = randint(1, 10)
    d2 = randint(1, 10)
    dfinal = (d1 + d2) * 100
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2}) * 100 T$')
    return dfinal

def dinheirorep4():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)
    d4 = randint(1, 6)
    dfinal = (d1 + d2 + d3 + d4) * 100
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2} + {d3} + {d4}) * 100 T$')
    return dfinal

def dinheirorep5():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)
    dfinal = (d1 + d2 + d3) * 1000
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2} + {d3}) * 1000 T$')
    return dfinal

def dinheirorep6():
    d1 = randint(1, 4)
    d2 = randint(1, 4)
    dfinal = (d1 + d2) * 1000
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2}) * 1000 TO')
    return dfinal


def dinheirondquarto(rolldinheiro):
    if rolldinheiro < 30:
        dinheirorep0()
        return 0
    elif rolldinheiro < 70:
        d1 = randint(1, 6)
        dfinal = f'{d1 * 10} TC'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} * 10 TC')
        return dfinal
    elif rolldinheiro < 95:
        d1 = randint(1, 4)
        dfinal = f'{d1 * 100} TC'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} * 100 TC')
        return dfinal
    else:
        d1 = randint(1, 6)
        dfinal = f'{d1 * 10} T$'
        sleep(0.4)
        print(f'O seu dinheiro rolou {d1} * 10 T$')
        return dfinal
