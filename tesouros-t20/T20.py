from random import randint
from time import sleep

def RolagensIniciais():
    global rolldinheiro
    global rollitem
    rolldinheiro = randint(1, 100)
    rollitem = randint(1, 100)
    sleep(0.4)
    print(f'Você rolou {rolldinheiro} para dinheiro e {rollitem} para item.')

def ndquarto():
    RolagensIniciais()

def ndmeio():
    RolagensIniciais()

def nd1():
    RolagensIniciais()

def nd2():
    RolagensIniciais()

def nd3():
    RolagensIniciais()

def nd4():
    RolagensIniciais()

def nd5():
    RolagensIniciais()

def nd6():
    RolagensIniciais()

def nd7():
    RolagensIniciais()

def nd8():
    RolagensIniciais()

def nd9():
    RolagensIniciais()

def nd10():
    RolagensIniciais()

def nd11():
    RolagensIniciais()

def nd12():
    RolagensIniciais()

def nd13():
    RolagensIniciais()

def nd14():
    RolagensIniciais()

def nd15():
    RolagensIniciais()

def nd16():
    RolagensIniciais()

def nd17():
    RolagensIniciais()

def nd18():
    RolagensIniciais()

def nd19():
    RolagensIniciais()

def nd20():
    RolagensIniciais()


def definirRolagem():
    tabelaND = [
        (0.25, ndquarto),
        (0.5, ndmeio),
        (1, nd1),
        (2, nd2),
        (3, nd3),
        (4, nd4),
        (5, nd5),
        (6, nd6),
        (7, nd7),
        (8, nd8),
        (9, nd9),
        (10, nd10),
        (11, nd11),
        (12, nd12),
        (13, nd13),
        (14, nd14),
        (15, nd15),
        (16, nd16),
        (17, nd17),
        (18, nd18),
        (19, nd19),
        (20, nd20),
    ]
    for nivel, nd in tabelaND:
        if nivel == NDTesouro:
            nd()
            break

#Programa Principal

while True:
    try:
        NDTesouro = str(input('Digite o ND do tesouro: ')).strip()
        if '/' in NDTesouro:
            numerador, denominador = map(int, NDTesouro.split('/'))
            NDTesouro = numerador / denominador
        else:
            NDTesouro = int(NDTesouro)
        if NDTesouro in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
            sleep(0.4)
            print(f'Você digitou o ND {NDTesouro}.')
            break
        elif NDTesouro == 0.25:
            sleep(0.4)
            print('Você digitou o ND 1/4.')
            break
        elif NDTesouro == 0.5:
            sleep(0.4)
            print('Você digitou o ND 1/2.')
            break
        else:
            print('Por favor, digite um ND válido.')
    except:
        print('Por favor, digite um ND válido.')

definirRolagem()