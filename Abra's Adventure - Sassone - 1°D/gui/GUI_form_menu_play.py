import pygame
from pygame.locals import *

from gui.GUI_button import Button
from gui.GUI_label import Label
from gui.GUI_button_image import Button_Image
from gui.GUI_form_menu_score import Form
from manejador_niveles import Manejador_niveles
from gui.GUI_form_contenedor_nivel import FormContenedorNivel


class FormMenuPlay(Form):
    def __init__(self, pantalla, x, y, w, h, color_background, color_border, border_size = -1, active=True, flag_home=True):
        super().__init__(pantalla, x, y, w, h, color_background, color_border, border_size, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        self.flag_home = flag_home
        self.x = x
        self.y = y
        self.w = w
        self.h = h


        #### CONTROLES ####
        self.btn_nv1 = Button_Image(self._slave,
                                    x,
                                    y,
                                    x=275,
                                    y=50,
                                    w=450,
                                    h=110,
                                    path_image="gui/UI_Flat_Button_Medium_Release_02a3.png",
                                    onclick=self.entrar_nivel,
                                    onclick_param="nivel_uno",
                                    font="assets\Early GameBoy.ttf",
                                    font_size=15,
                                    font_color="green3")
        self.btn_nv2 = Button_Image(self._slave,
                                    x,
                                    y,
                                    x=275,
                                    y=200,
                                    w=450,
                                    h=110,
                                    path_image="gui/UI_Flat_Button_Medium_Release_02a3.png",
                                    onclick=self.entrar_nivel,
                                    onclick_param="nivel_dos",
                                    font="assets\Early GameBoy.ttf",
                                    font_size=15,
                                    font_color="green3")
        self.btn_nv3 = Button_Image(self._slave,
                                    x,
                                    y,
                                    x=275,
                                    y=350,
                                    w=450,
                                    h=110,
                                    path_image="gui/UI_Flat_Button_Medium_Release_02a3.png",
                                    onclick=self.entrar_nivel,
                                    onclick_param="nivel_tres",
                                    font="assets\Early GameBoy.ttf",
                                    font_size=15,
                                    font_color="green3")
        self.btn_home = Button_Image(self._slave,
                                    x,
                                    y,
                                    x= 850,
                                    y= 400,
                                    w= 50,
                                    h= 50,
                                    path_image="gui/home.png",
                                    onclick=self.btn_home_click,
                                    onclick_param="",
                                    font="assets\Early GameBoy.ttf",
                                    font_size=15,
                                    font_color="green3")
        self.label_nv1 = Label(self._slave,
                                x=275,
                                y=50,
                                w=450,
                                h=110,
                                text="NIVEL 1",
                                font="assets\Early GameBoy.ttf",
                                font_size=25,
                                font_color="gray14",
                                path_image="gui/UI_Flat_Button_Medium_Release_02a3.png")
        self.label_nv2 = Label(self._slave,
                                x=275,
                                y=200,
                                w=450,
                                h=110,
                                text="NIVEL 2",
                                font="assets\Early GameBoy.ttf",
                                font_size=25,
                                font_color="gray14",
                                path_image="gui/UI_Flat_Button_Medium_Release_02a3.png")
        self.label_nv3 = Label(self._slave,
                                x=275,
                                y=350,
                                w=450,
                                h=110,
                                text="NIVEL 3",
                                font="assets\Early GameBoy.ttf",
                                font_size=25,
                                font_color="gray14",
                                path_image="gui/UI_Flat_Button_Medium_Release_02a3.png")

###############################################################

        #### AGREGO LOS CONTROLES A UNA LISTAS ####
        self.lista_widgets.append(self.btn_nv1)
        self.lista_widgets.append(self.btn_nv2)
        self.lista_widgets.append(self.btn_nv3)
        self.lista_widgets.append(self.label_nv1)
        self.lista_widgets.append(self.label_nv2)
        self.lista_widgets.append(self.label_nv3)
        if self.flag_home:
            self.lista_widgets.append(self.btn_home)
    

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        frm_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(frm_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()