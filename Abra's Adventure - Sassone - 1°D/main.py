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
from classes.class_nivel_1 import Nivel_1
from classes.class_nivel_2 import Nivel_2
from classes.class_nivel_3 import Nivel_3
#los ataques solo se muestran en el ultimo nivel importado. por que?
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

nivel_actual = Nivel_2(pantalla)

### Loop ##################################################################################################
while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
### pantalla START #########################################################################################
    if juego_activo:
        if flag_start:
            if pygame.key.get_pressed()[pygame.K_RETURN] == False:
                dibujar_start(pantalla)
            else:
                flag_start = False
### NIVEL ################################################################################################
        if flag_start == False:
            nivel_actual.update(eventos)
### Menu Pausa ##############################################################################################
    else:
        #form_prueba.update(eventos)
        if pygame.key.get_pressed()[pygame.K_SPACE] and juego_activo == False:
            juego_activo = True

    pygame.display.flip()
