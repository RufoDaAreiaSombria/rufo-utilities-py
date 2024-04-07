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
    armaduras = [(5, 'Couro'),
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
    (54, 'Material especial2'),
    (70, 'Poderoso'),
    (85, 'Potencializador'),
    (100, 'Vigilante')
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
    (46, 'Energética*'),
    (48, 'Excruciante'),
    (53, 'Flamejante'),
    (63, 'Formidável'),
    (64, 'Lancinante*'),
    (72, 'Magnífica*'),
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
    (16, 'Animado1'),
    (18, 'Assustador'),
    (22, 'Cáustica'),
    (32, 'Defensor'),
    (34, 'Escorregadio'),
    (36, 'Esmagador1'),
    (38, 'Fantasmagórico'),
    (40, 'Fortificado'),
    (44, 'Gélido'),
    (54, 'Guardião2'),
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
    (5, 'Azagaia dos relâmpagos'),
    (15, 'Espada baronial'),
    (25, 'Lâmina da luz'),
    (30, 'Lança animalesca'),
    (35, 'Maça do terror'),
    (40, 'Florete fugaz'),
    (45, 'Cajado da destruição'),
    (50, 'Cajado da vida'),
    (55, 'Machado silvestre'),
    (60, 'Martelo de Doherimm'),
    (67, 'Arco do poder'),
    (72, 'Língua do deserto'),
    (77, 'Besta explosiva'),
    (82, 'Punhal sszzaazita'),
    (87, 'Espada sortuda'),
    (92, 'Avalanche'),
    (95, 'Cajado do poder'),
    (100, 'Vingadora sagrada')
    ]

def itemespecifico():
    itemespecifico = [    
    (10, 'Cota élfica'),
    (20, 'Couro de monstro'),
    (25, 'Escudo do conjurador'),
    (32, 'Loriga do centurião'),
    (42, 'Manto da noite'),
    (49, 'Couraça do comando'),
    (59, 'Baluarte anão'),
    (66, 'Escudo espinhoso'),
    (76, 'Escudo do leão'),
    (83, 'Carapaça demoníaca'),
    (88, 'Escudo do eclipse'),
    (93, 'Escudo de Azgher'),
    (100, 'Armadura da luz')
    ]




