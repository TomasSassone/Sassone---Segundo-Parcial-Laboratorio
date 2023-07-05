import pygame
from configuraciones import obtener_rectangulos
from classes.class_enemigo import Enemigo
from classes.class_proyectil import Proyectil
import random

class Boss(Enemigo):
    def __init__(self, x, y, hp, animaciones, width, height, piso_der, velocidad, pantalla):
        self.hp = hp
        self.width = width
        self.height = height
        self.animaciones = animaciones
        self.x = x
        self.pantalla = pantalla
        self.reescalar_animaciones()
        self.contador_pasos = 0
        self.rectangulo = self.animaciones["boss_idle"][0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.bottom = y
        self.piso_der =  piso_der
        self.lados = obtener_rectangulos(self.rectangulo)
        self.velocidad = velocidad
        self.flag_orientacion = "derecha"
        self.hp = hp
        self.flag_dmg = False
        self.proyectiles = []
        self.flag_attack = False
    def spawnear_enemigo(self, target):
        if self.flag_attack:
            self.disparar_proyectil(target)
            self.flag_attack = False
        else:
            self.animar("boss_idle")
        self.realizar_dmg(target)
        for proyectil in self.proyectiles:
            proyectil.update(target)
    

    def restar_hp(self):
        if self.hp > -1:
            self.hp -= 1
            self.animar("boss_hit")
            print(self.hp)
            self.flag_attack = True
        return True
    
    def realizar_dmg(self, target):
        if self.rectangulo.colliderect(target.rectangulo):
            if target.hp > 0:
                if self.flag == False:
                    target.hp -= 1
                    self.flag = True
                    print(target.hp)
        else:
            self.flag = False

    def disparar_proyectil(self, target):
        proyectil = Proyectil(self.rectangulo.x, self.rectangulo.y+self.height/3, self.flag_orientacion, self.pantalla, self.animaciones, 4)
        proyectil.rect.x += proyectil.rect.width  # Ajustar la posición horizontal si el personaje está orientado hacia la izquierda
        self.proyectiles.append(proyectil)
        if proyectil.rect.colliderect(target.rectangulo):
            print("hit proyectil")