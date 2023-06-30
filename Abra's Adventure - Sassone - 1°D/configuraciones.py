import pygame
from constantes_pygame import *


def reescalar_imagenes(lista_original, width, height):
    for i in range(len(lista_original)):
        lista_original[i] = pygame.transform.scale(lista_original[i], (width, height))

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def obtener_rectangulos(principal)->dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return diccionario

personaje_idle =   [pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
]

personaje_idle_der = girar_imagenes(personaje_idle, True, False)

personaje_camina_izq = [pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/5 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/6 flota.png"),
]
personaje_camina = girar_imagenes(personaje_camina_izq, True, False)

personaje_salta =   [pygame.image.load("assets/abra - alakazam sprites/14 flota.png"),
                    pygame.image.load("assets/abra - alakazam sprites/14 flota.png")
]

personaje_salta_der = girar_imagenes(personaje_salta, True, False)

personaje_golpe_izq = [pygame.image.load("assets/abra - alakazam sprites/ataque_melee_1 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_1 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_1 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_2 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_2 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_2 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_3 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_3 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_3 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_4 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_4 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_4 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_4 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_5 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_5 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_5 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_5 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_6 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_6 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_6 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_6 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_7 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_7 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_7 flota.png"),
                                pygame.image.load("assets/abra - alakazam sprites/ataque_melee_7 flota.png")
                                ]

personaje_golpe = girar_imagenes(personaje_golpe_izq, True, False)

personaje_hit = [pygame.image.load("assets/abra - alakazam sprites/37.png"),
                pygame.image.load("assets/abra - alakazam sprites/37.png"),
                pygame.image.load("assets/abra - alakazam sprites/5.png"),
                pygame.image.load("assets/abra - alakazam sprites/5.png"),
                pygame.image.load("assets/abra - alakazam sprites/37.png"),
                pygame.image.load("assets/abra - alakazam sprites/37.png"),
                pygame.image.load("assets/abra - alakazam sprites/5.png"),
                pygame.image.load("assets/abra - alakazam sprites/5.png"),
                pygame.image.load("assets/abra - alakazam sprites/37.png"),
                pygame.image.load("assets/abra - alakazam sprites/37.png"),
                pygame.image.load("assets/abra - alakazam sprites/37.png"),
                ]

personaje_muerto = [pygame.image.load("assets/abra - alakazam sprites/72.png")
                ]

personaje_dispara = [pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_4.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_4.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_5.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_5.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_6.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_6.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_6.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_6.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_7.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_7.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_7.png"),
                    pygame.image.load("assets/abra - alakazam sprites/ataque_proyectil_7.png")
                    ]
personaje_dispara_der = girar_imagenes(personaje_dispara, True, False)

personaje_flotando = [pygame.image.load("assets/abra - alakazam sprites/flotando_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_1.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_2.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_3.png"),
                    pygame.image.load("assets/abra - alakazam sprites/flotando_3.png")
                    ]

personaje_flotando_der = girar_imagenes(personaje_flotando, True, False)

proyectil_derecha = [pygame.image.load("assets/proyectil abra/1.png"),
                    pygame.image.load("assets/proyectil abra/1.png"),
                    pygame.image.load("assets/proyectil abra/1.png"),
                    pygame.image.load("assets/proyectil abra/1.png"),
                    pygame.image.load("assets/proyectil abra/1.png"),
                    pygame.image.load("assets/proyectil abra/2.png"),
                    pygame.image.load("assets/proyectil abra/2.png"),
                    pygame.image.load("assets/proyectil abra/2.png"),
                    pygame.image.load("assets/proyectil abra/2.png"),
                    pygame.image.load("assets/proyectil abra/2.png"),
                    pygame.image.load("assets/proyectil abra/3.png"),
                    pygame.image.load("assets/proyectil abra/3.png"),
                    pygame.image.load("assets/proyectil abra/3.png"),
                    pygame.image.load("assets/proyectil abra/3.png"),
                    pygame.image.load("assets/proyectil abra/3.png"),
                    pygame.image.load("assets/proyectil abra/4.png"),
                    pygame.image.load("assets/proyectil abra/4.png"),
                    pygame.image.load("assets/proyectil abra/4.png"),
                    pygame.image.load("assets/proyectil abra/4.png"),
                    pygame.image.load("assets/proyectil abra/4.png"),
                    pygame.image.load("assets/proyectil abra/5.png"),
                    pygame.image.load("assets/proyectil abra/5.png"),
                    pygame.image.load("assets/proyectil abra/5.png"),
                    pygame.image.load("assets/proyectil abra/5.png"),
                    pygame.image.load("assets/proyectil abra/5.png"),
                    pygame.image.load("assets/proyectil abra/6.png"),
                    pygame.image.load("assets/proyectil abra/6.png"),
                    pygame.image.load("assets/proyectil abra/6.png"),
                    pygame.image.load("assets/proyectil abra/6.png"),
                    pygame.image.load("assets/proyectil abra/6.png"),
                    pygame.image.load("assets/proyectil abra/7.png"),
                    pygame.image.load("assets/proyectil abra/7.png"),
                    pygame.image.load("assets/proyectil abra/7.png"),
                    pygame.image.load("assets/proyectil abra/7.png"),
                    pygame.image.load("assets/proyectil abra/7.png"),
                    pygame.image.load("assets/proyectil abra/8.png"),
                    pygame.image.load("assets/proyectil abra/8.png"),
                    pygame.image.load("assets/proyectil abra/8.png"),
                    pygame.image.load("assets/proyectil abra/8.png"),
                    pygame.image.load("assets/proyectil abra/8.png"),
                    pygame.image.load("assets/proyectil abra/9.png"),
                    pygame.image.load("assets/proyectil abra/9.png"),
                    pygame.image.load("assets/proyectil abra/9.png"),
                    pygame.image.load("assets/proyectil abra/9.png"),
                    pygame.image.load("assets/proyectil abra/9.png"),
                    pygame.image.load("assets/proyectil abra/10.png"),
                    pygame.image.load("assets/proyectil abra/10.png"),
                    pygame.image.load("assets/proyectil abra/10.png"),
                    pygame.image.load("assets/proyectil abra/10.png"),
                    pygame.image.load("assets/proyectil abra/10.png"),
                    ]

proyectil_izquierda = girar_imagenes(proyectil_derecha, True, False)

pocion_idle = [pygame.image.load("assets/items/pocion/pocion_1.png"),
                pygame.image.load("assets/items/pocion/pocion_1.png"),
                pygame.image.load("assets/items/pocion/pocion_1.png"),
                pygame.image.load("assets/items/pocion/pocion_1.png"),
                pygame.image.load("assets/items/pocion/pocion_1.png"),
                pygame.image.load("assets/items/pocion/pocion_1.png"),
                pygame.image.load("assets/items/pocion/pocion_1.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_3.png"),
                pygame.image.load("assets/items/pocion/pocion_3.png"),
                pygame.image.load("assets/items/pocion/pocion_3.png"),
                pygame.image.load("assets/items/pocion/pocion_3.png"),
                pygame.image.load("assets/items/pocion/pocion_3.png"),
                pygame.image.load("assets/items/pocion/pocion_3.png"),
                pygame.image.load("assets/items/pocion/pocion_3.png"),
                pygame.image.load("assets/items/pocion/pocion_3.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png"),
                pygame.image.load("assets/items/pocion/pocion_2.png")
]

carameloraro_idle = [pygame.image.load("assets/items/carameloraro.png")

]

rocket_fem_camina_der = [pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (2).png"),
                pygame.image.load("assets/rocket secuaz/2 (2).png"),
                pygame.image.load("assets/rocket secuaz/2 (2).png"),
                pygame.image.load("assets/rocket secuaz/2 (2).png"),
                pygame.image.load("assets/rocket secuaz/2 (2).png"),
                pygame.image.load("assets/rocket secuaz/2 (3).png"),
                pygame.image.load("assets/rocket secuaz/2 (3).png"),
                pygame.image.load("assets/rocket secuaz/2 (3).png"),
                pygame.image.load("assets/rocket secuaz/2 (3).png"),
                pygame.image.load("assets/rocket secuaz/2 (3).png"),
]

rocket_fem_camina = girar_imagenes(rocket_fem_camina_der, True, False)

rocket_fem_hit_izq = [pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),
                pygame.image.load("assets/rocket secuaz/2 (1).png"),      
                pygame.image.load("assets/rocket secuaz/2 (1)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (1)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (1)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (1)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (2)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (2)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (2)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (2)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (2)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (3)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (3)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (3)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (3)_hit.png"),
                pygame.image.load("assets/rocket secuaz/2 (3)_hit.png"),
]

rocket_fem_idle = [
                pygame.image.load("assets/rocket secuaz/2 (3).png"),
]

sierra = [
    pygame.image.load("assets/rueda/rueda_1.png"),
    pygame.image.load("assets/rueda/rueda_1.png"),
    pygame.image.load("assets/rueda/rueda_1.png"),
    pygame.image.load("assets/rueda/rueda_1.png"),
    pygame.image.load("assets/rueda/rueda_1.png"),
    pygame.image.load("assets/rueda/rueda_2.png"),
    pygame.image.load("assets/rueda/rueda_2.png"),
    pygame.image.load("assets/rueda/rueda_2.png"),
    pygame.image.load("assets/rueda/rueda_2.png"),
    pygame.image.load("assets/rueda/rueda_2.png"),
    pygame.image.load("assets/rueda/rueda_3.png"),
    pygame.image.load("assets/rueda/rueda_3.png"),
    pygame.image.load("assets/rueda/rueda_3.png"),
    pygame.image.load("assets/rueda/rueda_3.png"),
    pygame.image.load("assets/rueda/rueda_3.png")
]

sierra_azul = [
    pygame.image.load("assets/rueda_azul/rueda_azul_1.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_1.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_1.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_1.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_1.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_2.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_2.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_2.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_2.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_2.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_3.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_3.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_3.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_3.png"),
    pygame.image.load("assets/rueda_azul/rueda_azul_3.png")
]

sierra_half = [
    pygame.image.load("assets/rueda_half/rueda_half_1.png"),
    pygame.image.load("assets/rueda_half/rueda_half_1.png"),
    pygame.image.load("assets/rueda_half/rueda_half_1.png"),
    pygame.image.load("assets/rueda_half/rueda_half_1.png"),
    pygame.image.load("assets/rueda_half/rueda_half_1.png"),
    pygame.image.load("assets/rueda_half/rueda_half_2.png"),
    pygame.image.load("assets/rueda_half/rueda_half_2.png"),
    pygame.image.load("assets/rueda_half/rueda_half_2.png"),
    pygame.image.load("assets/rueda_half/rueda_half_2.png"),
    pygame.image.load("assets/rueda_half/rueda_half_2.png"),
    pygame.image.load("assets/rueda_half/rueda_half_3.png"),
    pygame.image.load("assets/rueda_half/rueda_half_3.png"),
    pygame.image.load("assets/rueda_half/rueda_half_3.png"),
    pygame.image.load("assets/rueda_half/rueda_half_3.png"),
    pygame.image.load("assets/rueda_half/rueda_half_3.png")
]

sierra_half_volteada = girar_imagenes(sierra_half, False, True)

##############


# plataformas nivel 1
lv1_plat1_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (300, 30))
lv1_plat1 = pygame.Rect(850, 150, 300, 30)
lv1_lados_plat1 = obtener_rectangulos(lv1_plat1)

lv1_plat2_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (250, 30))
lv1_plat2 = pygame.Rect(500, 350, 250, 30)
lv1_lados_plat2 = obtener_rectangulos(lv1_plat2)

lv1_plat3_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (200, 30))
lv1_plat3 = pygame.Rect(100, 100, 200, 30)
lv1_lados_plat3 = obtener_rectangulos(lv1_plat3)

lv1_plat4_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (95, 30))
lv1_plat4 = pygame.Rect(130, 300, 95, 30)
lv1_lados_plat4 = obtener_rectangulos(lv1_plat4)

lista_plataformas_nivel_1 = [lv1_lados_plat1, lv1_lados_plat2, lv1_lados_plat3, lv1_lados_plat4]



# plataformas nivel 2

lv2_plat1_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (450, 30))
lv2_plat1 = pygame.Rect(400, 150, 450, 30)
lv2_lados_plat1 = obtener_rectangulos(lv2_plat1)

lv2_plat2_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (160, 30))
lv2_plat2 = pygame.Rect(300, 350, 160, 30)
lv2_lados_plat2 = obtener_rectangulos(lv2_plat2)

lv2_plat3_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (310, 30))
lv2_plat3 = pygame.Rect(90, 100, 310, 30)
lv2_lados_plat3 = obtener_rectangulos(lv2_plat3)

lista_plataformas_nivel_2 = [lv2_lados_plat1, lv2_lados_plat2, lv2_lados_plat3]

# plataformas nivel 3

lv3_plat1_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_labo_1.png"), (450, 30))
lv3_plat1 = pygame.Rect(400, 150, 450, 30)
lv3_lados_plat1 = obtener_rectangulos(lv3_plat1)

lv3_plat2_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_labo_1.png"), (160, 30))
lv3_plat2 = pygame.Rect(300, 350, 160, 30)
lv3_lados_plat2 = obtener_rectangulos(lv3_plat2)

lv3_plat3_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_labo_1.png"), (310, 30))
lv3_plat3 = pygame.Rect(90, 100, 310, 30)
lv3_lados_plat3 = obtener_rectangulos(lv3_plat3)

lista_plataformas_nivel_3 = [lv3_lados_plat1, lv3_lados_plat2, lv3_lados_plat3]




#diccionarios
diccionario_animaciones_jugador = {}
diccionario_animaciones_jugador['personaje_idle'] = personaje_idle
diccionario_animaciones_jugador['personaje_idle_der'] = personaje_idle_der
diccionario_animaciones_jugador['personaje_camina'] = personaje_camina
diccionario_animaciones_jugador['personaje_camina_izq'] = personaje_camina_izq
diccionario_animaciones_jugador['personaje_salta'] = personaje_salta
diccionario_animaciones_jugador['personaje_salta_der'] = personaje_salta_der
diccionario_animaciones_jugador['personaje_golpe'] = personaje_golpe
diccionario_animaciones_jugador['personaje_golpe_izq'] = personaje_golpe_izq
diccionario_animaciones_jugador['personaje_hit'] = personaje_hit
diccionario_animaciones_jugador['personaje_muerto'] = personaje_muerto
diccionario_animaciones_jugador['proyectil_derecha'] = proyectil_derecha
diccionario_animaciones_jugador['proyectil_izquierda'] = proyectil_izquierda
diccionario_animaciones_jugador['personaje_dispara'] = personaje_dispara
diccionario_animaciones_jugador['personaje_dispara_der'] = personaje_dispara_der
diccionario_animaciones_jugador['personaje_flotando'] = personaje_flotando
diccionario_animaciones_jugador['personaje_flotando_der'] = personaje_flotando_der

diccionario_animaciones_enemigo = {}
diccionario_animaciones_enemigo['rocket_fem_camina'] = rocket_fem_camina
diccionario_animaciones_enemigo['rocket_fem_camina_der'] = rocket_fem_camina_der
diccionario_animaciones_enemigo['rocket_fem_idle'] = rocket_fem_idle
diccionario_animaciones_enemigo['rocket_fem_hit_izq'] = rocket_fem_hit_izq

diccionario_animaciones_item = {}
diccionario_animaciones_item['pocion_idle'] = pocion_idle
diccionario_animaciones_item['carameloraro_idle'] = carameloraro_idle

diccionario_animaciones_trampas = {}
diccionario_animaciones_trampas['sierra'] = sierra
diccionario_animaciones_trampas['sierra_half'] = sierra_half
diccionario_animaciones_trampas['sierra_half_volteada'] = sierra_half_volteada
diccionario_animaciones_trampas['sierra_azul'] = sierra_azul