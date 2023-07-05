import pygame, sys
from pygame.locals import *
from modo import *
from hud import *
from configuraciones import obtener_rectangulos
from sql import *

scorepoints = 0

class Nivel():
    '''Clase principal que maneja los tres niveles, recibe una pantalla, el personaje del jugador, una lista de plataformas, enemigos, items y trampas,
        una imagen de fondo y una imagen de piso'''
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
        global scorepoints
        scorepoints = 0
        pygame.mixer.music.load("assets/sonidos/bw2_rival.mp3")
        pygame.mixer.music.play(-1)
        self.sonido_proyectil = pygame.mixer.Sound("assets/sonidos/ataque_melee_jugador.wav")
        self.canal1 = pygame.mixer.Channel(1)
        self.sonido_hit_enemigo = pygame.mixer.Sound("assets/sonidos/hit_enemigo.wav")
        self.canal2 = pygame.mixer.Channel(2)
        self.flag_sound_pause = False
        self.lista_canales_sonido = [self.canal1, self.canal2]

        self.puerta_salida = pygame.transform.scale(pygame.image.load("assets/door_close.png"), (45, 80))
        self.puerta_salida_abierta = pygame.transform.scale(pygame.image.load("assets/door_open.png"), (45, 80))
        self.puerta_salida_rect = pygame.Rect(1100, 400, 45, 80)
        self.lados_puerta = obtener_rectangulos(self.puerta_salida_rect)
        self.contador_enemigos_muertos = 0
        #texto
        self.texto_titulo = pygame.font.Font("assets\Early GameBoy.ttf", 40)
        self.texto_titulo = self.texto_titulo.render("LEVEL FINISHED", False, "whitesmoke").convert()
        self.texto_titulo_rect = self.texto_titulo.get_rect(center = (ANCHO_PANTALLA/2, ALTO_PANTALLA/2-100))
        #flags end level
        self.level_finished = False
        self.nivel_terminado = False


    def update(self, lista_eventos):
        '''actualiza eventos, detecciones de teclas, pantallas, enemigos, items, trampas y al mismo jugador'''
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                #ataque
                if evento.key == pygame.K_m:
                    for enemigo in self.enemigos:
                        self.jugador.atacar("golpe", enemigo)
                if evento.key == pygame.K_n:
                    for enemigo in self.enemigos:
                        self.jugador.atacar("proyectil", enemigo)
                        self.canal1.play(self.sonido_proyectil)
        if not self.nivel_terminado:
            self.actualizar_pantalla()
            self.jugador.movimiento()
            self.jugador.manejar_hp(self.lista_items)

    
    

    def actualizar_pantalla(self):
        '''actualiza la pantalla y spawnea todos los objetos del nivel'''
        global scorepoints
        self._slave.blit(self.img_fondo, (0,0))
        self._slave.blit(self.piso, (0,60))
        self._slave.blit(self.puerta_salida, (1100, 400))
        if self.level_finished:
            self._slave.blit(self.puerta_salida_abierta, (1100, 400))

        for plataforma in self.plataformas:
            self._slave.blit(plataforma['surf'], (plataforma['rect'].x, plataforma['rect'].y))

        for enemigo in self.enemigos:
            if enemigo.hp > 0:
                enemigo.spawnear_enemigo(self.jugador)

            if enemigo.hp == 0:
                self.canal2.play(self.sonido_hit_enemigo)
                enemigo.hp -= 1
                self.contador_enemigos_muertos += 1
                scorepoints += 20
                print(f"enemigos derrotados: {self.contador_enemigos_muertos}/{len(self.enemigos)}")

            if self.contador_enemigos_muertos == len(self.enemigos):
                self.level_finished = True
                editar_score(scorepoints)

        for item in self.lista_items:
            item.update()
            if self.jugador.lados['main'].colliderect(item.lados['main']):
                if item.key == "carameloraro_idle":
                    scorepoints += 15
                self.lista_items.remove(item)

        for trampa in self.lista_trampas:
            trampa.spawnear_trampa(self.jugador)

        tiempo_restante = dibujar_hud(self._slave, self.jugador.hp, scorepoints)
        if tiempo_restante <= 0:
            self.jugador.matar_jugador()

        if self.level_finished:
            if self.jugador.lados['main'].colliderect(self.lados_puerta['main']):
                self._slave.blit(self.texto_titulo, self.texto_titulo_rect)
                self.jugador.velocidad = 0
                self.nivel_terminado = True

        self.jugador.update(self.lados_piso, self.enemigos)

        return self.level_finished

    def dibujar_rectangulos(self):
        '''modo debug'''
        for lado in self.jugador.lados:
            pygame.draw.rect(self._slave, "red", self.jugador.lados[lado], 2)
        for plataforma in self.plataformas:
            for lado in plataforma['lados']:
                pygame.draw.rect(self._slave, "blue", plataforma['lados'][lado], 2)
        for enemigo in self.enemigos:
            for lado in enemigo.lados:
                pygame.draw.rect(self._slave, "green", enemigo.lados[lado], 1)

