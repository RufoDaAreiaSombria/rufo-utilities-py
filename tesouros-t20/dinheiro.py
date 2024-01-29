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
    print(f'O seu dinheiro rolou {d1} * 100 T$')
    return dfinal

def dinheirorep2():
    d1 = randint(1, 12)
    d2 = randint(1, 12)
    d3 = randint(1, 12)
    d4 = randint(1, 12)
    dfinal = f'{(d1 + d2 + d3 + d4) * 10} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2} + {d3} + {d4}) * 10 T$')
    return dfinal

def dinheirorep3():
    d1 = randint(1, 10)
    d2 = randint(1, 10)
    dfinal = f'{(d1 + d2) * 100} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2}) * 100 T$')
    return dfinal

def dinheirorep4():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)
    d4 = randint(1, 6)
    dfinal = f'{(d1 + d2 + d3 + d4) * 100} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2} + {d3} + {d4}) * 100 T$')
    return dfinal

def dinheirorep5():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)
    dfinal = f'{(d1 + d2 + d3) * 1000} T$'
    sleep(0.4)
    print(f'O seu dinheiro rolou ({d1} + {d2} + {d3}) * 1000 T$')
    return dfinal

def dinheirorep6():
    d1 = randint(1, 4)
    d2 = randint(1, 4)
    dfinal = f'{(d1 + d2) * 1000} T$'
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

    elif rolldinheiro < 60:
    
    elif rolldinheiro < 90:

    else:

def dinheirond4(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 50:

    elif rolldinheiro < 80:

    elif rolldinheiro < 90:

    else:

def dinheirond5(rolldinheiro):
    if rolldinheiro < 15:
        dinheirorep0()
        return 0
    elif rolldinheiro < 65:

    elif rolldinheiro < 95:

    else:

def dinheirond6(rolldinheiro):
    if rolldinheiro < 15:
        dinheirorep0()
        return 0
    elif rolldinheiro < 60:

    elif rolldinheiro < 90:

    else:

def dinheirond7(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 60:

    elif rolldinheiro < 90:

    else:

def dinheirond8(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 55:

    elif rolldinheiro < 95:

    else:

def dinheirond9(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 35:

    elif rolldinheiro < 85:

    else:

def dinheirond10(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 30:

    elif rolldinheiro < 85:

    else:

def dinheirond11(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 45:

    elif rolldinheiro < 85:

    else:

def dinheirond12(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 45:

    elif rolldinheiro < 80:

    else:

def dinheirond13(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 45:

    elif rolldinheiro < 80:

    else:

def dinheirond14(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 45:

    elif rolldinheiro < 80:

    else:

def dinheirond15(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 45:

    elif rolldinheiro < 80:

    else:

def dinheirond16(rolldinheiro):
    if rolldinheiro < 10:
        dinheirorep0()
        return 0
    elif rolldinheiro < 40:

    elif rolldinheiro < 75:

    else:

def dinheirond17(rolldinheiro):
    if rolldinheiro < 5:
        dinheirorep0()
        return 0
    elif rolldinheiro < 40:

    elif rolldinheiro < 75:

    else:

def dinheirond18(rolldinheiro):
    if rolldinheiro < 5:
        dinheirorep0()
        return 0
    elif rolldinheiro < 40:

    elif rolldinheiro < 75:

    else:

def dinheirond19(rolldinheiro):
    if rolldinheiro < 5:
        dinheirorep0()
        return 0
    elif rolldinheiro < 40:

    elif rolldinheiro < 75:

    else:

def dinheirond20(rolldinheiro):
    if rolldinheiro < 5:
        dinheirorep0()
        return 0
    elif rolldinheiro < 40:

    elif rolldinheiro < 75:

    else:

