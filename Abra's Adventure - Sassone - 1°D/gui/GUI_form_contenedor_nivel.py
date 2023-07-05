import pygame
from pygame.locals import *

from gui.GUI_form import *
from gui.GUI_button_image import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), "green", "black", -1, True) #pone 600 en vez de pantalla.get_width()
        nivel._slave = self._slave
        self.nivel = nivel
        self.btn_home = Button_Image(screen=self._slave,
                                    master_x= self._x,
                                    master_y= self._y,
                                    x = 50,
                                    y = 530,
                                    w = 30,
                                    h = 30,
                                    onclick= self.btn_home_click,
                                    onclick_param= "",
                                    path_image= "gui/home.png")
        self.btn_mute = Button_Image(screen=self._slave,
                                    master_x= self._x,
                                    master_y= self._y,
                                    x = 100,
                                    y = 530,
                                    w = 30,
                                    h = 30,
                                    onclick= self.btn_mute_click,
                                    onclick_param= "",
                                    path_image= "gui/btn_mute.png")
        
        self.flag_mute = True

        self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self.btn_home)
        self.lista_widgets.append(self.btn_mute)
        

    def update(self, lista_eventos):
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
        self.nivel.update(lista_eventos)

    def btn_home_click(self, param):
        self.end_dialog()

    def btn_mute_click(self, param):
        if self.flag_mute:
            # Silenciar el audio
            pygame.mixer.music.pause()
            pygame.mixer.pause()
            pygame.mixer.music.set_volume(0)  # Establecer volumen en 0
        else:
            # Restaurar el audio
            pygame.mixer.music.unpause()
            pygame.mixer.unpause()
            pygame.mixer.music.set_volume(1)  # Restaurar volumen original
        self.flag_mute = not self.flag_mute

