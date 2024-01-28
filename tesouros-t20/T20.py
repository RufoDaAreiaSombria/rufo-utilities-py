from random import randint
from time import sleep
from dinheiro import *

def RolagensIniciais():
    global rolldinheiro
    global rollitem
    rolldinheiro = randint(1, 100)
    rollitem = randint(1, 100)
    sleep(0.4)
    print(f'Você rolou {rolldinheiro} para dinheiro e {rollitem} para item.')

def ndquarto():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirondquarto(rolldinheiro)

def ndmeio():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirondmeio(rolldinheiro)

def nd1():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond1(rolldinheiro)

def nd2():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond2(rolldinheiro)

def nd3():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond3(rolldinheiro)

def nd4():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond4(rolldinheiro)

def nd5():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond5(rolldinheiro)

def nd6():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond6(rolldinheiro)

def nd7():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond7(rolldinheiro)

def nd8():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond8(rolldinheiro)

def nd9():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond9(rolldinheiro)

def nd10():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond10(rolldinheiro)

def nd11():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond11(rolldinheiro)

def nd12():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond12(rolldinheiro)

def nd13():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond13(rolldinheiro)

def nd14():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond14(rolldinheiro)

def nd15():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond15(rolldinheiro)

def nd16():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond16(rolldinheiro)

def nd17():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond17(rolldinheiro)

def nd18():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond18(rolldinheiro)

def nd19():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond19(rolldinheiro)

def nd20():
    global dfinal
    RolagensIniciais()
    dfinal = dinheirond20(rolldinheiro)


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
if dfinal != 0:
    sleep(0.4)
    print(f'O dinheiro encontrado nesse tesouro foi {dfinal}.')
else:
    sleep(0.4)
    print('Você não encontrou dinheiro nesse tesouro.')