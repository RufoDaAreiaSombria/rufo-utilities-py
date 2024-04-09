from random import randint
from time import sleep



def diversos():
    diversos = [
    (2, 'Ácido'),
    (4, 'Água benta'),
    (5, 'Alaúde élfico'),
    (6, 'Algemas'),
    (8, 'Baga-de-fogo'),
    (23, 'Bálsamo restaurador'),
    (24, 'Bandana'),
    (25, 'Bandoleira de poções'),
    (30, 'Bomba'),
    (31, 'Botas reforçadas'),
    (32, 'Camisa bufante'),
    (33, 'Capa esvoaçante'),
    (34, 'Capa pesada'),
    (35, 'Casaco longo'),
    (36, 'Chapéu arcano'),
    (38, 'Coleção de livros'),
    (40, 'Cosmético'),
    (42, 'Dente-de-dragão'),
    (43, 'Enfeite de elmo'),
    (44, 'Elixir do amor'),
    (46, 'Equipamento de viagem'),
    (56, 'Essência de mana'),
    (57, 'Estojo de disfarces'),
    (58, 'Farrapos de ermitão'),
    (59, 'Flauta mística'),
    (66, 'Fogo alquímico'),
    (67, 'Gorro de ervas'),
    (69, 'Líquen lilás'),
    (70, 'Luneta'),
    (73, 'Maleta de medicamentos'),
    (74, 'Manopla'),
    (75, 'Manto eclesiástico'),
    (78, 'Mochila de aventureiro'),
    (80, 'Musgo púrpura'),
    (83, 'Organizador de pergaminhos'),
    (85, 'Pó de cristal'),
    (87, 'Pó de giz'),
    (88, 'Pó do desaparecimento'),
    (89, 'Robe místico'),
    (91, 'Saco de sal'),
    (92, 'Sapatos de camurça'),
    (94, 'Seixo de âmbar'),
    (95, 'Sela'),
    (96, 'Tabardo'),
    (97, 'Traje da corte'),
    (99, 'Terra de cemitério'),
    (100, 'Veste de seda')
    ]

def armas():
    armas = [
    (3, 'Adaga'),
    (5, 'Alabarda'),
    (7, 'Alfange'),
    (10, 'Arco curto'),
    (13, 'Arco longo'),
    (15, 'Azagaia'),
    (16, 'Balas (20)'),
    (18, 'Besta leve'),
    (20, 'Besta pesada'),
    (23, 'Bordão'),
    (24, 'Chicote'),
    (27, 'Cimitarra'),
    (30, 'Clava'),
    (31, 'Corrente de espinhos'),
    (33, 'Espada bastarda'),
    (38, 'Espada curta'),
    (43, 'Espada longa'),
    (46, 'Flechas (20)'),
    (49, 'Florete'),
    (51, 'Foice'),
    (53, 'Funda'),
    (55, 'Gadanho'),
    (56, 'Katana'),
    (59, 'Lança'),
    (60, 'Lança montada'),
    (63, 'Maça'),
    (66, 'Machadinha'),
    (67, 'Machado anão'),
    (70, 'Machado de batalha'),
    (73, 'Machado de guerra'),
    (74, 'Machado táurico'),
    (76, 'Mangual'),
    (77, 'Marreta'),
    (80, 'Martelo de guerra'),
    (83, 'Montante'),
    (84, 'Mosquete'),
    (85, 'Pedras (20)'),
    (88, 'Picareta'),
    (90, 'Pique'),
    (92, 'Pistola'),
    (93, 'Rede'),
    (96, 'Tacape'),
    (98, 'Tridente'),
    (100, 'Virotes (20)')
]

def armaduras():
    armaduras = [
    (5, 'Couro'),
    (10, 'Brunea'),
    (25, 'Completa'),
    (30, 'Cota de malha'),
    (45, 'Couraça'),
    (55, 'Couro batido'),
    (65, 'Escudo leve'),
    (80, 'Escudo pesado'),
    (85, 'Gibão de peles'),
    (90, 'Loriga segmentada'),
    (100, 'Meia armadura')
]

def esotéricos():
    esotéricos = [
    (10, 'Bolsa de Pó'),
    (25, 'Cajado Arcano'),
    (35, 'Cetro Elemental'),
    (42, 'Costela de Lich'),
    (50, 'Dedo de Ente'),
    (55, 'Luva de Ferro'),
    (65, 'Medalhão de Prata'),
    (75, 'Orbe Cristalina'),
    (85, 'Tomo Hermético'),
    (100, 'Varinha Arcana')
]

def apriarma():
    apriarma = [
    (10, 'Atroz'),
    (13, 'Banhada a Ouro'),
    (23, 'Certeira'),
    (26, 'Cravejada de Gemas'),
    (36, 'Cruel'),
    (39, 'Discreta'),
    (44, 'Equilibrada'),
    (48, 'Harmonizada'),
    (53, 'Injeção Alquímica'),
    (55, 'Macabra'),
    (65, 'Maciça'),
    (75, 'Material Especial'),
    (80, 'Mira telescópica'),
    (90, 'Precisa'),
    (100, 'Pungente')
    ]

def apridura():
    apridura = [
    (15, 'Ajustada'),
    (19, 'Banhada a Ouro'),
    (23, 'Cravejada de Gemas'),
    (28, 'Delicada'),
    (32, 'Discreta'),
    (37, 'Espinhos'),
    (40, 'Macabra'),
    (50, 'Material Especial'),
    (55, 'Polida'),
    (80, 'Reforçada'),
    (90, 'Selada'),
    (100, 'Sob Medida')
    ]

def aprieso():
    aprieso = [
    (4, 'Banhada a ouro'),
    (8, 'Cravejada de gemas'),
    (12, 'Discreto'),
    (27, 'Energético'),
    (42, 'Harmonizado'),
    (45, 'Macabra'),
    (54, 'Material especial'),
    (70, 'Poderoso'),
    (85, 'Potencializador'),
    (100, 'Vigilante')
    ]

def poção():
    poção = [
    (15, 'Curar Ferimentos (2d8+2 PV)'),
    (18, 'Disfarce Ilusório'),
    (20, 'Escuridão (óleo)'),
    (22, 'Luz (óleo)'),
    (24, 'Névoa (granada)'),
    (26, 'Primor Atlético'),
    (28, 'Proteção Divina'),
    (30, 'Resistência a Energia'),
    (32, 'Sono'),
    (35, 'Visão Mística'),
    (36, 'Vitalidade Fantasma'),
    (38, 'Escudo da Fé (aprimoramento para duração cena)'),
    (40, 'Alterar Tamanho'),
    (42, 'Aparência Perfeita'),
    (43, 'Armamento da Natureza (óleo)'),
    (49, 'Bola de Fogo (granada)'),
    (51, 'Camuflagem Ilusória'),
    (53, 'Concentração de Combate (aprimoramento para duração cena)'),
    (62, 'Curar Ferimentos (4d8+4 PV)'),
    (66, 'Físico Divino'),
    (68, 'Mente Divina'),
    (70, 'Metamorfose'),
    (75, 'Purificação'),
    (77, 'Velocidade'),
    (79, 'Vestimenta da Fé (óleo)'),
    (80, 'Voz Divina'),
    (82, 'Arma Mágica (óleo; aprimoramento para bônus +3)'),
    (88, 'Curar Ferimentos (7d8+7 PV)'),
    (89, 'Físico Divino (aprimoramento para três atributos)'),
    (92, 'Invisibilidade (aprimoramento para duração cena)'),
    (96, 'Bola de Fogo (granada; aprimoramento para 10d6 de dano)'),
    (100, 'Curar Ferimentos (11d8+11 PV)')
]

def encantoarma():
    encantoarma = [
    (5, 'Ameaçadora'),
    (10, 'Anticriatura'),
    (12, 'Arremesso'),
    (14, 'Assassina'),
    (16, 'Caçadora'),
    (21, 'Congelante'),
    (23, 'Conjuradora'),
    (28, 'Corrosiva'),
    (30, 'Dançarina'),
    (34, 'Defensora'),
    (36, 'Destruidora'),
    (38, 'Dilacerante'),
    (40, 'Drenante'),
    (45, 'Elétrica'),
    (46, 'Energética'),
    (48, 'Excruciante'),
    (53, 'Flamejante'),
    (63, 'Formidável'),
    (64, 'Lancinante'),
    (72, 'Magnífica'),
    (74, 'Piedosa'),
    (76, 'Profana'),
    (78, 'Sagrada'),
    (80, 'Sanguinária'),
    (82, 'Trovejante'),
    (84, 'Tumular'),
    (88, 'Veloz'),
    (90, 'Venenosa'),
    (100, 'Arma Específica')
    ]

def encantodura():
    encantodura = [
    (6, 'Abascanto'),
    (10, 'Abençoado'),
    (12, 'Acrobático'),
    (14, 'Alado'),
    (16, 'Animado'),
    (18, 'Assustador'),
    (22, 'Cáustica'),
    (32, 'Defensor'),
    (34, 'Escorregadio'),
    (36, 'Esmagador'),
    (38, 'Fantasmagórico'),
    (40, 'Fortificado'),
    (44, 'Gélido'),
    (54, 'Guardião'),
    (56, 'Hipnótico'),
    (58, 'Ilusório'),
    (62, 'Incandescente'),
    (68, 'Invulnerável'),
    (72, 'Opaco'),
    (78, 'Protetor'),
    (80, 'Refletor'),
    (84, 'Relampejante'),
    (86, 'Reluzente'),
    (88, 'Sombrio'),
    (90, 'Zeloso')
    (100, 'Item Específico')
    ]

def armaespecifica():
    armaespecifica = [
    (5, 'Azagaia dos Relâmpagos'),
    (15, 'Espada Baronial'),
    (25, 'Lâmina da Luz'),
    (30, 'Lança Animalesca'),
    (35, 'Maça do Terror'),
    (40, 'Florete Fugaz'),
    (45, 'Cajado da Destruição'),
    (50, 'Cajado da Vida'),
    (55, 'Machado Silvestre'),
    (60, 'Martelo de Doherimm'),
    (67, 'Arco do Poder'),
    (72, 'Língua do Deserto'),
    (77, 'Besta Explosiva'),
    (82, 'Punhal Sszzaazita'),
    (87, 'Espada Sortuda'),
    (92, 'Avalanche'),
    (95, 'Cajado do Poder'),
    (100, 'Vingadora Sagrada')
    ]

def itemespecifico():
    itemespecifico = [    
    (10, 'Cota Élfica'),
    (20, 'Couro de Monstro'),
    (25, 'Escudo do Conjurador'),
    (32, 'Loriga do Centurião'),
    (42, 'Manto da Noite'),
    (49, 'Couraça do Comando'),
    (59, 'Baluarte Anão'),
    (66, 'Escudo Espinhoso'),
    (76, 'Escudo do Leão'),
    (83, 'Carapaça Demoníaca'),
    (88, 'Escudo do Eclipse'),
    (93, 'Escudo de Azgher'),
    (100, 'Armadura da Luz')
    ]

def acessmenor():
    acessmenor = [
    (2, 'Anel do Sustento'),
    (7, 'Bainha Mágica'),
    (12, 'Corda da Escalada'),
    (14, 'Ferraduras da Velocidade'),
    (19, 'Garrafa da Fumaça Eterna'),
    (24, 'Gema da Luminosidade'),
    (29, 'Manto Élfico'),
    (34, 'Mochila de Carga'),
    (40, 'Brincos da Sagacidade'),
    (46, 'Luvas da Delicadeza'),
    (52, 'Manoplas da Força do Ogro'),
    (59, 'Manto da Resistência'),
    (65, 'Manto do Fascínio'),
    (71, 'Pingente da Sensatez'),
    (77, 'Torque do Vigor'),
    (82, 'Chapéu do Disfarce'),
    (84, 'Flauta Fantasma'),
    (89, 'Lanterna da Revelação'),
    (96, 'Anel da Proteção'),
    (98, 'Anel do Escudo Mental'),
    (100, 'Pingente da Saúde')
    ]

def acessmedio():
    acessmedio = [
    (4, 'Anel de Telecinesia'),
    (8, 'Bola de Cristal'),
    (10, 'Caveira Maldita'),
    (14, 'Botas Aladas'),
    (18, 'Braceletes de Bronze'),
    (24, 'Anel da Energia'),
    (30, 'Anel da Vitalidade'),
    (34, 'Anel de Invisibilidade'),
    (38, 'Braçadeiras do Arqueiro'),
    (42, 'Brincos de Marah'),
    (46, 'Faixas do Pugilista'),
    (50, 'Manto da Aranha'),
    (54, 'Vassoura Voadora'),
    (58, 'Símbolo Abençoado'),
    (64, 'Amuleto da Robustez'),
    (68, 'Botas Velozes'),
    (74, 'Cinto da Força do Gigante'),
    (80, 'Coroa Majestosa'),
    (86, 'Estola da Serenidade'),
    (88, 'Manto do Morcego'),
    (94, 'Pulseiras da Celeridade'),
    (100, 'Tiara da Sapiência')
    ]

def acessmaior():
    acessmaior = [
    (2, 'Elmo do Teletransporte'),
    (4, 'Gema da Telepatia'),
    (9, 'Gema Elemental'),
    (15, 'Manual da Saúde Corporal'),
    (21, 'Manual do Bom Exercício'),
    (27, 'Manual dos Movimentos Precisos'),
    (34, 'Medalhão de Lena'),
    (40, 'Tomo da Compreensão'),
    (46, 'Tomo da Liderança e Influência'),
    (52, 'Tomo dos Grandes Pensamentos'),
    (57, 'Anel Refletor'),
    (60, 'Cinto do Campeão'),
    (67, 'Colar Guardião'),
    (72, 'Estatueta Animista'),
    (77, 'Anel da Liberdade'),
    (82, 'Tapete Voador'),
    (87, 'Braceletes de Ouro'),
    (89, 'Espelho da Oposição'),
    (94, 'Robe do Arquimago'),
    (96, 'Orbe das Tempestades'),
    (98, 'Anel da Regeneração'),
    (100, 'Espelho do Aprisionamento')
    ]

def itemrep0():
    sleep(0.4)
    print('Sua rolagem de item não rendeu nada.')

def itemrep1():
    

def itemrep2():
    

def itemrep3():
    

def itemrep4():
    

def itemrep5():
    
    
def itemndquarto(rollitem):
    if rollitem <= 50:
        itemrep0()
        return ''
    elif rollitem <= 75:
        sleep(0.4)
        print('Você conseguiu um item Diverso')
        return itemrep1()
    else:
        sleep(0.4)
        print('Você conseguiu um Equipamento')
        return itemrep2()

def itemndmeio(rollitem):
    if rollitem <= 45:
        itemrep0()
        return ''
    elif rollitem <= 70:
        sleep(0.4)
        print('Você conseguiu um item Diverso')
        return itemrep1()
    else:
        sleep(0.4)
        print('Você conseguiu um Equipamento')
        return itemrep2()

def itemnd1(rollitem):
    if rollitem <= 40:
        itemrep0()
        return ''
    elif rollitem <= 65:
        sleep(0.4)
        print('Você conseguiu um item Diverso')
        return itemrep1()
    elif rollitem <= 90:
        sleep(0.4)
        print('Você conseguiu um Equipamento')
        return itemrep2()
    else:
        sleep(0.4)
        print('Você conseguiu 1 poção')
        return itemrep4(1, 0)

def itemnd2(rollitem):
    if rollitem <= 30:
        itemrep0()
        return ''
    elif rollitem <= 40:
        sleep(0.4)
        print('Você conseguiu um item Diverso')
        return itemrep1()
    elif rollitem <= 70:
        sleep(0.4)
        print('Você conseguiu um Equipamento')
        return itemrep2()
    elif rollitem <= 90:
        sleep(0.4)
        print('Você conseguiu 1 poção')
        return itemrep4(1, 0)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 1 Aprimoramento')
        return itemrep3(1)

def itemnd3(rollitem):
    if rollitem <= 25:
        itemrep0()
        return ''
    elif rollitem <= 35:
        sleep(0.4)
        print('Você conseguiu um item Diverso')
        return itemrep1()
    elif rollitem <= 60:
        sleep(0.4)
        print('Você conseguiu um Equipamento')
        return itemrep2()
    elif rollitem <= 85:
        sleep(0.4)
        print('Você conseguiu 1 poção')
        return itemrep4(1, 0)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 1 Aprimoramento')
        return itemrep3(1)

def itemnd4(rollitem):
    if rollitem <= 20:
        itemrep0()
        return ''
    elif rollitem <= 30:
        sleep(0.4)
        print('Você conseguiu um item Diverso')
        return itemrep1()
    elif rollitem <= 55:
        sleep(0.4)
        print('Você conseguiu um Equipamento')
        return itemrep2()
    elif rollitem <= 80:
        sleep(0.4)
        print('Você conseguiu 1 poção')
        return itemrep4(1, 20)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 1 Aprimoramento')
        return itemrep3(1)

def itemnd5(rollitem):
    if rollitem <= 20:
        itemrep0()
        return ''
    elif rollitem <= 70:
        sleep(0.4)
        print('Você conseguiu 1 poção')
        return itemrep4(1, 0)
    elif rollitem <= 90:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 1 Aprimoramento')
        return itemrep3(1)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 2 Aprimoramentos')
        return itemrep3(2)

def itemnd6(rollitem):
    if rollitem <= 20:
        itemrep0()
        return ''
    elif rollitem <= 65:
        sleep(0.4)
        print('Você conseguiu 1 poção')
        return itemrep4(1, 20)
    elif rollitem <= 95:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 1 Aprimoramento')
        return itemrep3(1)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 2 Aprimoramentos')
        return itemrep3(2)

def itemnd7(rollitem):
    if rollitem <= 20:
        itemrep0()
        return ''
    elif rollitem <= 60:
        sleep(0.4)
        print('Você conseguiu 1d3 poções')
        return itemrep4(2, 0)
    elif rollitem <= 90:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 2 Aprimoramento')
        return itemrep3(2)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 3 Aprimoramentos')
        return itemrep3(3)

def itemnd8(rollitem):
    if rollitem <= 20:
        itemrep0()
        return ''
    elif rollitem <= 75:
        sleep(0.4)
        print('Você conseguiu 1d3 poções')
        return itemrep4(2, 0)
    elif rollitem <= 95:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 2 Aprimoramento')
        return itemrep3(2)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 3 Aprimoramentos')
        return itemrep3(3)

def itemnd9(rollitem):
    if rollitem <= 20:
        itemrep0()
        return ''
    elif rollitem <= 70:
        sleep(0.4)
        print('Você conseguiu 1 poção')
        return itemrep4(1, 20)
    elif rollitem <= 95:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 3 Aprimoramentos')
        return itemrep3(3)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Menor')
        return itemrep5(1)
    
def itemnd10(rollitem):
    if rollitem <= 50:
        itemrep0()
        return ''
    elif rollitem <= 75:
        sleep(0.4)
        print('Você conseguiu 1d3+1 poções')
        return itemrep4(3, 0)
    elif rollitem <= 90:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 3 Aprimoramentos')
        return itemrep3(3)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Menor')
        return itemrep5(1)

def itemnd11(rollitem):
    if rollitem <= 45:
        itemrep0()
        return ''
    elif rollitem <= 70:
        sleep(0.4)
        print('Você conseguiu 1d4+1 poções')
        return itemrep4(4, 0)
    elif rollitem <= 90:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 3 Aprimoramentos')
        return itemrep3(3)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Menor')
        return itemrep5(1)

def itemnd12(rollitem):
    if rollitem <= 45:
        itemrep0()
        return ''
    elif rollitem <= 70:
        sleep(0.4)
        print('Você conseguiu 1d3+1 poções')
        return itemrep4(3, 20)
    elif rollitem <= 85:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 4 Aprimoramentos')
        return itemrep3(4)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Menor')
        return itemrep5(1)

def itemnd13(rollitem):
    if rollitem <= 40:
        itemrep0()
        return ''
    elif rollitem <= 65:
        sleep(0.4)
        print('Você conseguiu 1d4+1 poções')
        return itemrep4(4, 20)
    elif rollitem <= 95:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 4 Aprimoramentos')
        return itemrep3(4)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Médio')
        return itemrep5(2)

def itemnd14(rollitem):
    if rollitem <= 40:
        itemrep0()
        return ''
    elif rollitem <= 65:
        sleep(0.4)
        print('Você conseguiu 1d4+1 poções')
        return itemrep4(4, 20)
    elif rollitem <= 90:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 4 Aprimoramentos')
        return itemrep3(4)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Médio')
        return itemrep5(2)

def itemnd15(rollitem):
    if rollitem <= 35:
        itemrep0()
        return ''
    elif rollitem <= 45:
        sleep(0.4)
        print('Você conseguiu 1d6+1 poções')
        return itemrep4(5, 0)
    elif rollitem <= 85:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 4 Aprimoramentos')
        return itemrep3(4)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Médio')
        return itemrep5(2)

def itemnd16(rollitem):
    if rollitem <= 35:
        itemrep0()
        return ''
    elif rollitem <= 45:
        sleep(0.4)
        print('Você conseguiu 1d6+1 poções')
        return itemrep4(5, 20)
    elif rollitem <= 80:
        sleep(0.4)
        print('Você conseguiu um Item Superior com 4 Aprimoramentos')
        return itemrep3(4)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Médio')
        return itemrep5(2)

def itemnd17(rollitem):
    if rollitem <= 20:
        itemrep0()
        return ''
    elif rollitem <= 40:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Menor')
        return itemrep5(1)
    elif rollitem <= 80:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Médio')
        return itemrep5(2)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Maior')
        return itemrep5(3)

def itemnd18(rollitem):
    if rollitem <= 15:
        itemrep0()
        return ''
    elif rollitem <= 40:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Menor')
        return itemrep5(1)
    elif rollitem <= 70:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Médio')
        return itemrep5(2)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Maior')
        return itemrep5(3)

def itemnd19(rollitem):
    if rollitem <= 10:
        itemrep0()
        return ''
    elif rollitem <= 40:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Menor')
        return itemrep5(1)
    elif rollitem <= 60:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Médio')
        return itemrep5(2)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Maior')
        return itemrep5(3)

def itemnd20(rollitem):
    if rollitem <= 5:
        itemrep0()
        return ''
    elif rollitem <= 40:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Menor')
        return itemrep5(1)
    elif rollitem <= 50:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Médio')
        return itemrep5(2)
    else:
        sleep(0.4)
        print('Você conseguiu um Item Mágico Maior')
        return itemrep5(3)

