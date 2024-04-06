from random import randint #Usado pra rolar os dados aleatórios
from time import sleep #Uma pequena espera pra ficar mais legal
from dinheiro import * #O arquivo da parte de riqueza do tesouro
from item import * #O arquivo da parte de itens do tesouro

#Os primeiros dois d100 que se rolam
def RolagensIniciais():
    global rolldinheiro
    global rollitem
    rolldinheiro = randint(1, 100)
    rollitem = randint(1, 100)
    sleep(0.4)
    print(f'Você rolou {rolldinheiro} para dinheiro e {rollitem} para item.')

#Funções para cada ND dependendo do que for selecionado
def ndquarto():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirondquarto(rolldinheiro)
    ifinal = itemndquarto(rollitem)

def ndmeio():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirondmeio(rolldinheiro)
    ifinal = itemndmeio(rollitem)

def nd1():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond1(rolldinheiro)
    ifinal = itemnd1(rollitem)

def nd2():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond2(rolldinheiro)
    ifinal = itemnd2(rollitem)

def nd3():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond3(rolldinheiro)
    ifinal = itemnd3(rollitem)

def nd4():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond4(rolldinheiro)
    ifinal = itemnd4(rollitem)

def nd5():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond5(rolldinheiro)
    ifinal = itemnd5(rollitem)

def nd6():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond6(rolldinheiro)
    ifinal = itemnd6(rollitem)

def nd7():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond7(rolldinheiro)
    ifinal = itemnd7(rollitem)

def nd8():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond8(rolldinheiro)
    ifinal = itemnd8(rollitem)

def nd9():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond9(rolldinheiro)
    ifinal = itemnd9(rollitem)

def nd10():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond10(rolldinheiro)
    ifinal = itemnd10(rollitem)

def nd11():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond11(rolldinheiro)
    ifinal = itemnd11(rollitem)

def nd12():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond12(rolldinheiro)
    ifinal = itemnd12(rollitem)

def nd13():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond13(rolldinheiro)
    ifinal = itemnd13(rollitem)

def nd14():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond14(rolldinheiro)
    ifinal = itemnd14(rollitem)

def nd15():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond15(rolldinheiro)
    ifinal = itemnd15(rollitem)

def nd16():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond16(rolldinheiro)
    ifinal = itemnd16(rollitem)

def nd17():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond17(rolldinheiro)
    ifinal = itemnd17(rollitem)

def nd18():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond18(rolldinheiro)
    ifinal = itemnd18(rollitem)

def nd19():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond19(rolldinheiro)
    ifinal = itemnd19(rollitem)

def nd20():
    global dfinal
    global ifinal
    RolagensIniciais()
    dfinal = dinheirond20(rolldinheiro)
    ifinal = itemnd20(rollitem)


def definirRolagem(): #Lista dos números linkados com a função correspondente
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
        if nivel == NDTesouro: #Se o nível for igual ao valor escolhido pelo usuário
            nd() #Chama a função correspondente ao número
            break

#Programa Principal

while True: #Loop infinito até digitar um ND correto
    try: #Testa se o ND foi digitado corretamente
        NDTesouro = str(input('Digite o ND do tesouro: ')).strip() #Armazena o ND digitado
        if '/' in NDTesouro: #Vê se existe uma barra no ND digitado, tipo 1/4
            numerador, denominador = map(int, NDTesouro.split('/')) #Retira as barras da fração
            NDTesouro = numerador / denominador #Realiza a divisão com as partes da fração
        else:
            NDTesouro = int(NDTesouro) #Converte o ND para inteiro
        if NDTesouro in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: #Caso o ND escolhido seja de 1 a 20
            sleep(0.4)
            print(f'Você digitou o ND {NDTesouro}.')
            break
        elif NDTesouro == 0.25: #Caso o ND escolhido seja 1/4
            sleep(0.4)
            print('Você digitou o ND 1/4.')
            break
        elif NDTesouro == 0.5: #Caso o ND escolhido seja 1/2
            sleep(0.4)
            print('Você digitou o ND 1/2.')
            break
        else:
            print('Por favor, digite um ND válido.')
    except: #Acontece caso o ND não seja correto
        print('Por favor, digite um ND válido.')

definirRolagem() #Chama a função referente ao ND escolhido

if dfinal != 0: #Caso haja tesouro na rolagem
    sleep(0.4)
    print(f'O dinheiro encontrado nesse tesouro foi {dfinal}.')
else: #Caso não haja tesouro na rolagem
    sleep(0.4)
    print('Você não encontrou dinheiro nesse tesouro.')
if ifinal != "":
    sleep(0.4)
    print(f'O item encontrado nesse tesouro foi {ifinal}.')
else:
    sleep(0.4)
    print('Você não encontrou nenhum item nesse tesouro.')