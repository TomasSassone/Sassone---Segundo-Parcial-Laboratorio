import pygame
from configuraciones import *
from modo import *

class Item:
    def __init__(self, width, height, x, y, animaciones:dict, key:str, pantalla):
        self.width = width
        self.height = height
        #animaciones
        self.contador_pasos = 0
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.key = key
        #rectangulo
        self.rectangulo = self.animaciones[key][0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.bottom = y
        self.lados = obtener_rectangulos(self.rectangulo)
        self.pantalla = pantalla

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], self.width, self.height)
    
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], self.width, self.height)
    
    def animar(self, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        self.pantalla.blit(animacion[self.contador_pasos], self.lados['main'])
        self.contador_pasos += 1
    
    def update(self):
        self.animar(self.key)
        if get_modo():
            pygame.draw.rect(self.pantalla, "orange", self.rectangulo, 2)