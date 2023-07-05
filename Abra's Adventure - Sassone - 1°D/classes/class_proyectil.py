import pygame
from pygame.locals import *
from modo import get_modo
from configuraciones import diccionario_animaciones_jugador, diccionario_animaciones_boss
class Proyectil:
    def __init__(self, x, y, orientacion, pantalla, animaciones:dict, speed=3):
        if animaciones == diccionario_animaciones_boss:
            self.image = pygame.image.load("assets/proyectil_boss/1.png")  # Carga la imagen del proyectil
        elif animaciones == diccionario_animaciones_jugador:
            self.image = pygame.image.load("assets/proyectil abra/1.png")  # Carga la imagen del proyectil
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed  # Velocidad del proyectil
        self.orientacion = orientacion
        self.pantalla = pantalla
        self.flag_hit_proyectil = False
        #animaciones
        self.contador_pasos = 0
        self.animaciones = animaciones

    def animar(self, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        self.pantalla.blit(animacion[self.contador_pasos], self.rect)
        self.contador_pasos += 1    
    
    def update(self, enemigo):
        if self.orientacion:
            self.rect.x -= self.speed
            self.animar("proyectil_izquierda")
        else:
            self.rect.x += self.speed
            self.animar("proyectil_derecha")
        if self.rect.colliderect(enemigo.rectangulo):
            if self.flag_hit_proyectil == False:
                enemigo.restar_hp()
                self.flag_hit_proyectil = True
        if get_modo():
            pygame.draw.rect(self.pantalla, "blue", self.rect, 2)