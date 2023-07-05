import pygame
from constantes_pygame import *
from configuraciones import reescalar_imagenes, obtener_rectangulos
from classes.class_proyectil import Proyectil
from modo import *

class Personaje:
    def __init__(self, width:int, height:int, x, y, hp:int, animaciones:dict, velocidad:int, pantalla, lista_plataformas):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.pantalla = pantalla
        self.vel_y = 0
        self.hp = hp
        #gravedad
        self.gravedad = 0.7
        self.potencia_salto = -17
        self.limite_vel_caida = 20
        self.esta_saltando = False
        #animaciones
        self.contador_pasos = 0
        self.que_hace = "idle"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #rectangulos
        self.rectangulo = self.animaciones["personaje_camina"][0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.lados = obtener_rectangulos(self.rectangulo)
        #movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        self.flag_orientacion = False
        #ataque
        self.flag_hit = False
        self.flag_muriendo =  False
        self.proyectiles = []
        self.esta_flotando = False
        self.lista_plataformas = lista_plataformas


# HABILIDADES PERSONAJE: ataque melee, proyectil, salto, caida lenta manteniendo shift
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

    def update(self, piso, lista_enemigos):
        if not self.flag_muriendo:
            match self.que_hace:
                case "derecha":
                    if not self.esta_saltando:
                        self.animar("personaje_camina")
                    self.mover(self.velocidad)
                case "izquierda":
                    if not self.esta_saltando:
                        self.animar("personaje_camina_izq")
                    self.mover(-self.velocidad)
                case "idle":
                    if not self.esta_saltando:
                        if self.flag_orientacion:
                            self.animar("personaje_idle")
                        else:
                            self.animar("personaje_idle_der")
                case "salta":
                    if not self.esta_saltando:
                        if self.esta_flotando:
                            if self.flag_orientacion:
                                self.animar("personaje_flotando")
                            else:
                                self.animar("personaje_flotando_der")
                        else:
                            if self.flag_orientacion:
                                self.animar("personaje_salta")
                            else:
                                self.animar("personaje_salta_der")
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto
                case "proyectil":
                    if self.flag_orientacion:
                        self.animar("personaje_dispara")
                    else:
                        self.animar("personaje_dispara_der")
                case "golpe":
                    if not self.esta_saltando:
                        for enemigo in lista_enemigos:
                            self.atacar("golpe", enemigo)
                case "golpea":
                    if not self.esta_saltando:
                        if self.flag_orientacion:
                            self.animar("personaje_golpe_izq")
                        else:
                            self.animar("personaje_golpe")
            if self.que_hace == "muere":
                self.animar("personaje_muerto")

        for proyectil in self.proyectiles:
            for enemigo in lista_enemigos:
                proyectil.update(enemigo)
                
        self.aplicar_gravedad(piso)
        if get_modo():
            pygame.draw.rect(self.pantalla, "blue", self.rectangulo, 2)


    def movimiento(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rectangulo.right < ANCHO_PANTALLA - self.velocidad/2:
            self.que_hace = "derecha"
            self.flag_orientacion = False
        elif keys[pygame.K_a] and self.rectangulo.left > 0 + self.velocidad/2:
            self.que_hace = "izquierda"
            self.flag_orientacion = True
        else:
            self.que_hace = "idle"
        if keys[pygame.K_w]:
            self.que_hace = "salta"
        if keys[pygame.K_m]:
            self.que_hace = "golpea"
        if keys[pygame.K_n]:
            self.que_hace = "proyectil"
        if self.esta_saltando == True:
            if keys[pygame.K_LSHIFT]:
                self.limite_vel_caida = 3
                self.esta_flotando = True
            else:
                self.limite_vel_caida = 20
                self.esta_flotando = False


    def aplicar_gravedad(self, piso):
        #salto
        if self.esta_saltando:
            if self.esta_flotando:
                if self.flag_orientacion:
                    self.animar("personaje_flotando")
                else:
                    self.animar("personaje_flotando_der")
            else:
                if self.flag_orientacion:
                    self.animar("personaje_salta")
                else:
                    self.animar("personaje_salta_der")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_vel_caida:
                self.desplazamiento_y += self.gravedad
            
        if self.lados["bottom"].colliderect(piso['top']):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados['main'].bottom = piso['main'].top
        elif self.lista_plataformas != []:
            for plataforma in self.lista_plataformas:
                if self.lados["bottom"].colliderect(plataforma['lados']['top']):
                    self.desplazamiento_y = 0
                    self.esta_saltando = False
                    self.lados['main'].bottom = plataforma['lados']['main'].top + 5
                    break
                else:
                    self.esta_saltando = True
        


    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad


    def disparar_proyectil(self, enemigo):
        proyectil = Proyectil(self.rectangulo.x, self.rectangulo.y, self.flag_orientacion, self.pantalla, self.animaciones)
        if self.flag_orientacion:
            proyectil.rect.x += self.width  # Ajustar la posición horizontal si el personaje está orientado hacia la derecha
        else:
            proyectil.rect.x += proyectil.rect.width  # Ajustar la posición horizontal si el personaje está orientado hacia la izquierda
        self.proyectiles.append(proyectil)


    def atacar(self, tipo_ataque, enemigo):
        if not self.flag_muriendo:
            if tipo_ataque == "golpe":
                self.que_hace = "golpe"
                golpe = pygame.Rect(self.rectangulo.x - 40, self.rectangulo.y - 40, self.width+80, self.height+80)
                if golpe.colliderect(enemigo.rectangulo):
                    enemigo.restar_hp()
                if get_modo():
                    pygame.draw.rect(self.pantalla, "blue", golpe, 2)
            if tipo_ataque == "proyectil":
                self.que_hace = "proyectil"
                self.disparar_proyectil(enemigo)


    def manejar_hp(self, lista_items):
        for item in lista_items:
            if item.key == 'pocion_idle':
                if self.hp <= 3:
                    if self.lados["main"].colliderect(item.lados['main']) and self.hp < 3:
                        self.hp += 1
        if self.hp <= 0:
            self.matar_jugador()
    
    def restar_hp(self):
        self.hp -= 1
        if self.hp <= 0:
            self.matar_jugador()


    def matar_jugador(self):
        self.animar("personaje_muerto")
        self.flag_muriendo = True