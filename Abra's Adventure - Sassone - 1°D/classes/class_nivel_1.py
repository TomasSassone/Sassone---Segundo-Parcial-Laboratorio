import pygame, sys
from pygame.locals import *
from configuraciones import *
from classes.class_enemigo import Enemigo
from classes.class_nivel import *
from classes.class_personaje import Personaje
from classes.class_item import Item
from classes.class_trampa import Trampa

class Nivel_1(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        
        W = pantalla.get_width()
        H = pantalla.get_height()

        # FONDO
        fondo = pygame.transform.scale(pygame.image.load("assets/fondo_laboratorio.png"), (W, H))

        # plataformas nivel 1
        plat1_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (300, 30))
        plat1 = pygame.Rect(850, 150, 300, 30)
        lados_plat1 = obtener_rectangulos(plat1)

        plat2_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (250, 30))
        plat2 = pygame.Rect(500, 350, 250, 30)
        lados_plat2 = obtener_rectangulos(plat2)

        plat3_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (200, 30))
        plat3 = pygame.Rect(100, 100, 200, 30)
        lados_plat3 = obtener_rectangulos(plat3)

        plat4_surf = pygame.transform.scale(pygame.image.load("assets/plataforma_verde.png"), (95, 30))
        plat4 = pygame.Rect(130, 300, 95, 30)
        lados_plat4 = obtener_rectangulos(plat4)

        plat_1 = {'surf': plat1_surf, 'rect': plat1, 'lados': lados_plat1}
        plat_2 = {'surf': plat2_surf, 'rect': plat2, 'lados': lados_plat2}
        plat_3 = {'surf': plat3_surf, 'rect': plat3, 'lados': lados_plat3}
        plat_4 = {'surf': plat4_surf, 'rect': plat4, 'lados': lados_plat4}
        lista_plataformas = [plat_1, plat_2, plat_3, plat_4]

        #ENEMIGOS
        enemigo1 = Enemigo(lados_plat2['left'].left, lados_plat2['top'].top, 6, diccionario_animaciones_enemigo, 30, 50, lados_plat2['right'].right, 2, pantalla)
        enemigo2 = Enemigo(lados_plat3['left'].left, lados_plat3['top'].top, 6, diccionario_animaciones_enemigo, 30, 50, lados_plat3['right'].right, 1, pantalla)
        enemigo3 = Enemigo(lados_plat1['main'].left, lados_plat1['top'].top, 6, diccionario_animaciones_enemigo, 30, 50, lados_plat1['right'].right, 3, pantalla)
        lista_enemigos = [enemigo1, enemigo2, enemigo3]

        # Items
        pocion_1 = Item(30, 30, lados_plat4['left'].left + 50, lados_plat4['top'].top -1, diccionario_animaciones_item, 'pocion_idle', pantalla)
        pocion_2 = Item(30, 30, lados_plat3['left'].left + 10, lados_plat3['top'].top -1, diccionario_animaciones_item, 'pocion_idle', pantalla)
        carameloraro_1 = Item(30, 35, lados_plat1['left'].left + 50, lados_plat1['top'].top -1, diccionario_animaciones_item, 'carameloraro_idle', pantalla)
        lista_items = [pocion_1, pocion_2, carameloraro_1]

        # Trampas
        lista_trampas = []

        mi_personaje = Personaje(40, 50, 150, 440, 3, diccionario_animaciones_jugador, 5, pantalla, lista_plataformas)

        super().__init__(pantalla, mi_personaje, lista_plataformas, fondo, "assets/piso_laboratorio.png", lista_enemigos, lista_items, lista_trampas)
