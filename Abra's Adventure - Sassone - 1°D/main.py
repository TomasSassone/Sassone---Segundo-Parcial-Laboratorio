import pygame
import sys
from pygame.locals import *
from pantalla_start import dibujar_start
from constantes_pygame import *
from gui.GUI_form_settings import FormSettings
from sql import *
from modo import cambiar_modo

# Inicializa Pygame
pygame.init()

# Declara reloj y dimensiones de la pantalla
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

# Declaro la flag de la pantalla de start
flag_start = True

# Creo el objeto del formulario del menu principal
form_principal = FormSettings(pantalla, ANCHO_PANTALLA/2-400, ALTO_PANTALLA/2-200, 800,400, "dodgerblue4", "cyan3", 5, True)


# Crea la base de datos
crear_base()


# Loop # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Debug mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()
    
    # Pantalla de start
    if flag_start:
            if pygame.key.get_pressed()[pygame.K_RETURN] == False:
                dibujar_start(pantalla)
            else:
                flag_start = False

    # Menu principal
    else:
        pantalla.blit(pygame.transform.scale(pygame.image.load("assets/fondo_start_frames/frame_01_delay-0.1s.png"), (ANCHO_PANTALLA, ALTO_PANTALLA)), (0,0))
        form_principal.update(eventos)

        
    pygame.display.flip()