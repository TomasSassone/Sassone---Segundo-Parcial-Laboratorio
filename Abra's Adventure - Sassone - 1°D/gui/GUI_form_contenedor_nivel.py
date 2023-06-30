import pygame
from pygame.locals import *

from gui.GUI_form import *
from gui.GUI_button_image import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), "black", "black", 1, True) #pone 600 en vez de pantalla.get_width()
        nivel._slave = self._slave
        self.nivel = nivel

    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        self.draw()