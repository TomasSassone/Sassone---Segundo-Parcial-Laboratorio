import pygame, sys
from pygame.locals import *
from modo import *
from hud import *
from configuraciones import obtener_rectangulos

class Nivel():
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo, imagen_piso, lista_enemigos, lista_items, lista_trampas):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.img_piso = imagen_piso
        self.enemigos = lista_enemigos
        self.lista_items = lista_items
        self.lista_trampas = lista_trampas

        self.piso = pygame.image.load(self.img_piso).convert_alpha()
        self.piso_rect = pygame.Rect(0, 0, 1600, 20)
        self.piso_rect.top = self.jugador.lados['main'].bottom
        self.lados_piso = obtener_rectangulos(self.piso_rect)
        self.scorepoints = 0
        
        
        


    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    self.dibujar_rectangulos()
                    print("tab")
                if evento.key == pygame.K_v:
                    print(pygame.mouse.get_pos())
                #ataque
                if evento.key == pygame.K_m:
                    for enemigo in self.enemigos:
                        self.jugador.atacar("golpe", enemigo)
                if evento.key == pygame.K_n:
                    for enemigo in self.enemigos:
                        self.jugador.atacar("proyectil", enemigo)
                        
        self.actualizar_pantalla()
        self.jugador.movimiento()
        self.jugador.manejar_hp(self.lista_items)
        #pygame.mixer.init()
        #pygame.mixer.music.load("assets/sonidos/bw2-rival.mp3")
        #pygame.mixer.music.play(-1)
        #pygame.mixer.music.set_volume(0.1)
    
    def dibujar_rectangulos(self):
        if get_modo() == True:
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "red", self.jugador.lados[lado], 2)
            for plataforma in self.plataformas:
                for lado in plataforma['lados']:
                    pygame.draw.rect(self._slave, "blue", plataforma['lados'][lado], 2)
            for enemigo in self.enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self._slave, "green", enemigo.lados[lado], 2)
    

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))
        self._slave.blit(self.piso, (0,60))

        for plataforma in self.plataformas:
            self._slave.blit(plataforma['surf'], (plataforma['rect'].x, plataforma['rect'].y))
        for enemigo in self.enemigos:
            if enemigo.hp >= 0:
                enemigo.spawnear_enemigo(self.jugador)
        for item in self.lista_items:
            item.update()
            if self.jugador.lados['main'].colliderect(item.lados['main']):
                if item.key == "carameloraro_idle":
                    self.scorepoints += 50
                self.lista_items.remove(item)
        for trampa in self.lista_trampas:
            trampa.spawnear_trampa(self.jugador)
        tiempo_restante = dibujar_hud(self._slave, self.jugador.hp, self.scorepoints)
        if tiempo_restante <= 0:
            self.jugador.matar_jugador()
        

        self.jugador.update(self.lados_piso, self.enemigos)



