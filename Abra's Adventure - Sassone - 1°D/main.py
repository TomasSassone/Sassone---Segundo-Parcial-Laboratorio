import pygame, sys, random
from pygame.locals import *
from classes.class_imagen import *
from classes.class_personaje import *
from classes.class_plataforma import *
from classes.class_item import *
from constantes_pygame import *
from configuraciones import *
from pantalla_start import *
from modo import *
#from gui.GUI_form_prueba import FormInicio
from gui.GUI_form_principal import FormInicio

import sqlite3

'''
with sqlite3.connect("mi_base.db") as conexion:
    try:
        pass
    except Exception as e:
        pass
'''

#lista de colores: https://www.pygame.org/docs/ref/color_list.html

### Setup #################################################################################
pygame.init()
RELOJ = pygame.time.Clock()

flag_start = True
juego_activo = True

form_inicio = FormInicio(pantalla, 200, 175, 900, 350, "gold", "magenta", 5, True)
#form_inicio = FormInicio()
#form_prueba = FormInicio(pantalla, ANCHO_PANTALLA/2-400, ALTO_PANTALLA/2-250, 800, 500, "crimson", "blue", 3, True)
#form_select_nivel.nivel_actual = [Nivel_1(pantalla), Nivel_2(pantalla), Nivel_3(pantalla)]
#nivel_actual = Nivel_1(pantalla)

### Loop ##################################################################################################
while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    #form_select_nivel.lista_eventos = eventos
    for evento in eventos:
        if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                    juego_activo = False
### pantalla START #########################################################################################
    if juego_activo:
        if flag_start:
            if pygame.key.get_pressed()[pygame.K_RETURN] == False:
                dibujar_start(pantalla)
            else:
                flag_start = False
### NIVEL ################################################################################################
        if flag_start == False:
            form_inicio.update(eventos)
### Menu Pausa ##############################################################################################
    else:
        #form_pausa.update(eventos)
        if pygame.key.get_pressed()[pygame.K_SPACE] and juego_activo == False:
            juego_activo = True

    pygame.display.flip()

    #SE ESTA BLITEANDO EL FONDO DELANTE DE TODO
