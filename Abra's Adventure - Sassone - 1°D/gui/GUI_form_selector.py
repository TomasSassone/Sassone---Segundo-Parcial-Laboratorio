import pygame
from pygame.locals import *
from gui.GUI_form_menu_play import FormMenuPlay, Form

class FormSelector(Form):
    def __init__(self, pantalla, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(pantalla, x, y, w, h, color_background, color_border, border_size, active)
        #volumen y mixer
        self.volumen = 0.1
        self.flag_play = True
        pygame.mixer.init()



    def render(self):
        self._slave.fill(self._color_background)


    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                self.btn_jugar_click("")
        else:
            self.hijo.update(lista_eventos)


    def btn_jugar_click(self, param):
        frm_jugar = FormMenuPlay(pantalla=self._master,
                                x = self._master.get_width() / 2 - 500,
                                y = self._master.get_height() / 2 - 250,
                                w = 1000,
                                h = 500,
                                color_background= "crimson",
                                color_border = "chartreuse",
                                border_size=2,
                                active = True,
                                flag_home=False
                                )
        self.show_dialog(frm_jugar)
