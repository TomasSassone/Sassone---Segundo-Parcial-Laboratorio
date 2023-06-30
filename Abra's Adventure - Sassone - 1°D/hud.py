import pygame
from constantes_pygame import *
from configuraciones import reescalar_imagenes

lista_barra_vida = [pygame.image.load("assets/iconos_vida/vida_full.png"),
                    pygame.image.load("assets/iconos_vida/vida_2.png"),
                    pygame.image.load("assets/iconos_vida/vida_1.png"),
                    pygame.image.load("assets/iconos_vida/vida_vacia.png")
]

reescalar_imagenes(lista_barra_vida, 84, 26)

#temporizador
tiempo_actual = 0
temporizador = 30

def dibujar_hud(pantalla, vidas:int, scorepoints):
    #score
    score_surf = pygame.font.Font("assets\Early GameBoy.ttf", 15)
    score = score_surf.render(f"SCORE: {scorepoints}", False, "whitesmoke").convert_alpha()
    score_rect = score.get_rect(topright = (ANCHO_PANTALLA-20, 20))

    tiempo_actual = pygame.time.get_ticks()

    tiempo_restante = temporizador - tiempo_actual//1000
    if tiempo_restante <= 0:
        
        tiempo_restante = 0

    #temporizador
    if tiempo_restante >= 10:
        mensaje_temporizador = f"00:{tiempo_restante}"
    else:
        mensaje_temporizador = f"00:0{tiempo_restante}"
    temporizador_surf = pygame.font.Font("assets\Early GameBoy.ttf", 15)
    temporizador_text = temporizador_surf.render(mensaje_temporizador, False, "whitesmoke").convert_alpha()
    temporizador_rect = temporizador_text.get_rect(midtop = (ANCHO_PANTALLA//2, 20))
    

    match vidas:
        case 3:
            pantalla.blit(lista_barra_vida[0], (20,20))
        case 2:
            pantalla.blit(lista_barra_vida[1], (20,20))
        case 1:
            pantalla.blit(lista_barra_vida[2], (20,20))
        case _:
            pantalla.blit(lista_barra_vida[3], (20,20))
    pantalla.blit(score, score_rect)
    pantalla.blit(temporizador_text, temporizador_rect)
    return tiempo_restante