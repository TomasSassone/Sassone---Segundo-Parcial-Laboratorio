from configuraciones import obtener_rectangulos
from classes.class_personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, x, y, hp, animaciones, width, height, piso_der, velocidad, pantalla):
        self.hp = hp
        self.width = width
        self.height = height
        self.animaciones = animaciones
        self.x = x
        self.pantalla = pantalla
        self.reescalar_animaciones()
        self.contador_pasos = 0
        self.rectangulo = self.animaciones["rocket_fem_camina"][0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.bottom = y
        self.piso_der =  piso_der
        self.lados = obtener_rectangulos(self.rectangulo)
        self.velocidad = velocidad
        self.flag_orientacion = "derecha"
        self.hp = hp
        self.flag_dmg = False

    def spawnear_enemigo(self, target):
        if self.rectangulo.x + self.width >= self.piso_der:
            self.flag_orientacion = "izquierda"
        if self.rectangulo.x <= self.x:
            self.flag_orientacion = "derecha"
        if self.flag_orientacion == "derecha":
            self.mover(self.velocidad)
            self.animar("rocket_fem_camina")
        else:
            self.mover((self.velocidad)*-1)
            self.animar("rocket_fem_camina_der")
        self.realizar_dmg(target)
    

    def restar_hp(self):
        if self.hp > -1:
            self.hp -= 1
            self.animar("rocket_fem_hit_izq")
            print(self.hp)
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