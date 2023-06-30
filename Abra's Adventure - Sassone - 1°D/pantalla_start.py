import pygame
from constantes_pygame import *
from classes.class_imagen import *

pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)

abra_inicio = pygame.image.load("assets/abra - alakazam sprites/14.png").convert_alpha()
abra_inicio = pygame.transform.scale(abra_inicio, (150, 150))
abra_pos = abra_inicio.get_rect(center = (ANCHO_PANTALLA/2, 350))
flag_bajando = True

pygame.mixer.init()
pygame.mixer.music.load("assets/sonidos/Pokémon Fire Red - Title Screen (HQ).mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)

#abra pantalla de inicio
fondo_start = Imagen("assets/fondo_start_frames/frame_00_delay-0.1s.png", ANCHO_PANTALLA, ALTO_PANTALLA, 0,0, pantalla)
fondo_start = Imagen.cargar_imagen(fondo_start)

game_over_pantalla_fade = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
game_over_pantalla_fade.fill((0, 0, 0))
game_over_pantalla_fade.set_alpha(60)

def dibujar_start(pantalla):
    global flag_bajando

    pantalla.blit(fondo_start, (0,0))
    pantalla.blit(game_over_pantalla_fade, (0, 0))

    #caption e icono
    pygame.display.set_caption("Abra's Adventure")
    icono = pygame.image.load("assets/abra - alakazam sprites/6.png")
    pygame.display.set_icon(icono)

    texto_titulo = pygame.font.Font("assets\Early GameBoy.ttf", 60)
    texto_titulo_outline = pygame.font.Font("assets\Early GameBoy.ttf", 60)
    boton_start = pygame.font.Font("assets\Early GameBoy.ttf", 40)
    boton_start_outline = pygame.font.Font("assets\Early GameBoy.ttf", 40)
    controles = pygame.font.Font("assets\Early GameBoy.ttf", 10)


    #surfaces
    #titulo
    texto_titulo = texto_titulo.render("ABRA'S ADVENTURE", False, "whitesmoke").convert() #"whitesmoke"
    texto_titulo_rect = texto_titulo.get_rect(center = (ANCHO_PANTALLA/2, 180))
    #titulo outline
    texto_titulo_outline = texto_titulo_outline.render("ABRA'S ADVENTURE", False, (5, 26, 8)).convert()
    texto_titulo_outline_rect = texto_titulo_outline.get_rect(center = (ANCHO_PANTALLA/2, 186))
    #start
    boton_start = boton_start.render("PRESS ENTER", False, "whitesmoke").convert()
    boton_start_rect = boton_start.get_rect(center = (ANCHO_PANTALLA/2, 270))
    #start outline
    boton_start_outline = boton_start_outline.render("PRESS ENTER", False, (5, 26, 8)).convert()
    boton_start_outline_rect = boton_start_outline.get_rect(center = (ANCHO_PANTALLA/2, 274))
    #controles
    controles = controles.render("desplazamiento: WASD - Ataque Melee: M - Proyectil: N - Levitacion: mantener SHIFT", False, "antiquewhite").convert() #"whitesmoke"
    controles_rect = texto_titulo.get_rect(center = (ANCHO_PANTALLA/2+100, ALTO_PANTALLA-30))


    
    #screen.blit(ground_surface, (0,550))
    pantalla.blit(texto_titulo_outline, texto_titulo_outline_rect)
    pantalla.blit(texto_titulo, texto_titulo_rect)
    pantalla.blit(boton_start_outline, boton_start_outline_rect)
    pantalla.blit(boton_start, boton_start_rect)
    pantalla.blit(controles, controles_rect)
    #abra startpantalla
    if flag_bajando:
        abra_pos.y += 1 #baja
        if abra_pos.y == 300:
            flag_bajando = False
    else:
        abra_pos.y -= 1
        if abra_pos.y == 270:
            flag_bajando = True
    pantalla.blit(abra_inicio, (abra_pos.x, abra_pos.y))