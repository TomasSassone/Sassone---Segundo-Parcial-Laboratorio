import pygame
from pygame.locals import *
from configuraciones import obtener_rectangulos
from classes.class_enemigo import Enemigo

class Trampa(Enemigo):
    def __init__(self, x, y, animaciones, width, height, piso_der, pantalla, velocidad, tipo_sierra) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animaciones = animaciones
        self.pantalla = pantalla
        self.reescalar_animaciones()
        self.contador_pasos = 0
        self.rectangulo = self.animaciones['sierra'][0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.bottom = y
        self.lados = obtener_rectangulos(self.rectangulo)
        self.flag_dmg = False
        self.velocidad = velocidad
        self.piso_der = piso_der
        self.flag_orientacion = "derecha"
        self.tipo_sierra = tipo_sierra

    def spawnear_trampa(self, target):
        if self.rectangulo.x + self.width >= self.piso_der:
            self.flag_orientacion = "izquierda"
        if self.rectangulo.x <= self.x:
            self.flag_orientacion = "derecha"
        if self.flag_orientacion == "derecha":
            self.mover(self.velocidad)
        else:
            self.mover((self.velocidad)*-1)
        if self.tipo_sierra == "half":
            self.animar('sierra_half')
        elif self.tipo_sierra == "full":
            self.animar('sierra')
        elif self.tipo_sierra == "half_volteada":
            self.animar('sierra_half_volteada')
        self.realizar_dmg(target)    

    def realizar_dmg(self, target):
            if self.rectangulo.colliderect(target.rectangulo):
                if target.hp > 0:
                    if self.flag == False:
                        target.hp -= 1
                        self.flag = True
                        print(target.hp)
            else:
                self.flag = False