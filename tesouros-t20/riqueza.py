from random import randint
from time import sleep

def riquezamenor(porcento):
    ricroll = randint(1+porcento, 100+porcento)
    ricmenor = [
        ((1, 25), riqueza1),
        ((26, 40), riqueza2),
        ((41, 55), riqueza3),
        ((56, 70), riqueza4),
        ((71, 85), riqueza5),
        ((86, 95), riqueza6),
        ((96, 99), riqueza7),
        ((100, 120), riqueza8),
    ]
    for roll, ric in ricmenor:
        if roll[0] <= ricroll <= roll[1]:
            sleep(0.4)
            print(f'O dado de uma riqueza foi {ricroll}')
            return ric()
            break

def riquezamedia(porcento):
    ricroll = randint(1+porcento, 100+porcento)
    ricmedia = [
        ((1, 10), riqueza3),
        ((11, 30), riqueza4),
        ((31, 50), riqueza5),
        ((51, 65), riqueza6),
        ((66, 80), riqueza7),
        ((81, 90), riqueza8),
        ((91, 95), riqueza9),
        ((96, 99), riqueza10),
        ((100, 120), riqueza11)
    ]
    for roll, ric in ricmedia:
        if roll[0] <= ricroll <= roll[1]:
            sleep(0.4)
            print(f'O dado de uma riqueza foi {ricroll}')
            return ric()
            break

def riquezamaior(porcento):
    ricroll = randint(1+porcento, 100+porcento)
    ricmaior = [
        ((1, 5), riqueza5),
        ((6, 15), riqueza6),
        ((16, 25), riqueza7),
        ((26, 40), riqueza8),
        ((41, 60), riqueza9),
        ((61, 75), riqueza10),
        ((76, 85), riqueza11),
        ((86, 95), riqueza12),
        ((96, 120), riqueza13)
    ]
    for roll, ric in ricmaior:
        if roll[0] <= ricroll <= roll[1]:
            sleep(0.4)
            print(f'O dado de uma riqueza foi {ricroll}')
            return ric()
            break

def riqueza1():
    d1 = randint(1, 4)
    d2 = randint(1, 4)
    d3 = randint(1, 4)
    d4 = randint(1, 4)
    dfinal = f'{d1 + d2 + d3 + d4} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2} + {d3} + {d4}) T$')
    return dfinal

def riqueza2():
    d1 = randint(1, 4)
    dfinal = f'{d1 * 10} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou {d1} x 10 T$')
    return dfinal

def riqueza3():
    d1 = randint(1, 4)
    d2 = randint(1, 4)
    dfinal = f'{(d1 + d2) * 10} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2}) x 10 T$')
    return dfinal

def riqueza4():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)
    d4 = randint(1, 6)
    dfinal = f'{(d1 + d2 + d3 + d4) * 10} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2} + {d3} + {d4}) x 10 T$')
    return dfinal

def riqueza5():
    d1 = randint(1, 6)
    dfinal = f'{d1 * 100} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou {d1} x 100 T$')
    return dfinal

def riqueza6():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    dfinal = f'{(d1 + d2) * 100} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2}) x 100 T$')
    return dfinal

def riqueza7():
    d1 = randint(1, 8)
    d2 = randint(1, 8)
    dfinal = f'{(d1 + d2) * 100} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2}) x 100 T$')
    return dfinal

def riqueza8():
    d1 = randint(1, 10)
    d2 = randint(1, 10)
    d3 = randint(1, 10)
    d4 = randint(1, 10)
    dfinal = f'{(d1 + d2 + d3 + d4) * 100} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2} + {d3} + {d4}) x 100 T$')
    return dfinal

def riqueza9():
    d1 = randint(1, 12)
    d2 = randint(1, 12)
    d3 = randint(1, 12)
    d4 = randint(1, 12)
    d5 = randint(1, 12)
    d6 = randint(1, 12)
    dfinal = f'{(d1 + d2 + d3 + d4 + d5 + d6) * 100} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2} + {d3} + {d4} + {d5} + {d6}) x 100 T$')
    return dfinal

def riqueza10():
    d1 = randint(1, 10)
    d2 = randint(1, 10)
    dfinal = f'{(d1 + d2) * 1000} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2}) x 1.000 T$')
    return dfinal

def riqueza11():
    d1 = randint(1, 8)
    d2 = randint(1, 8)
    d3 = randint(1, 8)
    d4 = randint(1, 8)
    d5 = randint(1, 8)
    d6 = randint(1, 8)
    dfinal = f'{(d1 + d2 + d3 + d4 + d5 + d6) * 1000} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2} + {d3} + {d4} + {d5} + {d6}) x 1.000 T$')
    return dfinal

def riqueza12():
    d1 = randint(1, 10)
    dfinal = f'{d1 * 10000} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou {d1} x 10.000 T$')
    return dfinal

def riqueza13():
    d1 = randint(1, 12)
    d2 = randint(1, 12)
    d3 = randint(1, 12)
    d4 = randint(1, 12)
    dfinal = f'{(d1 + d2 + d3 + d4) * 10000} T$'
    sleep(0.4)
    print(f'Uma riqueza rolou ({d1} + {d2} + {d3} + {d4}) x 10.000 T$')
    return dfinal

