import pygame
from pygame.locals import *
from sql import *

from gui.GUI_button import Button
from gui.GUI_slider import Slider
from gui.GUI_textbox import TextBox
from gui.GUI_label import Label
from gui.GUI_form import Form
from gui.GUI_button_image import Button_Image
from gui.GUI_form_menu_score import FormMenuScore
from gui.GUI_form_menu_play import FormMenuPlay
from classes.class_nivel import *

class FormSettings(Form):
    def __init__(self, pantalla, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(pantalla, x, y, w, h, color_background, color_border, border_size, active)
        #volumen y mixer
        self.volumen = 0.1
        self.flag_play = True
        self.flag_mute = False
        pygame.mixer.init()
        #### CONTROLES ####
        self.txt_box = TextBox(self._slave, x, y, 100, 50, 100, 30, "whitesmoke", "white", "azure2", "forestgreen", 3, "assets\Early GameBoy.ttf", 10, "black")
        self.btn_txt = Button(self._slave, x, y, 210, 50, 70, 30, "aquamarine4", "blue", self.btn_guardar_nombre_click, "", "SAVE", "assets\Early GameBoy.ttf", 9, "whitesmoke")
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "brown3", "green", self.btn_play_click, "Nombre", "Pausa", font="assets\Early GameBoy.ttf", font_size=15, font_color="whitesmoke")
        self.label_volumen = Label(self._slave, 650, 190, 80, 50, "15", "assets\Early GameBoy.ttf", 15,"black", "gui/UI_Flat_Button_Medium_Release_02a3.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "blue", "white")
        self.btn_tabla = Button_Image(self._slave, x, y, 255, 100, 50, 50, "gui/Menu_BTN.png", self.btn_tabla_click, "x")
        self.btn_jugar = Button_Image(self._slave, x, y, 500, 230, 60, 60, "gui/Window.png", self.btn_jugar_click, "a", font="assets\Early GameBoy.ttf", font_size=15, font_color="whitesmoke")
        self.btn_on_off = Button_Image(self._slave, x, y, 400, 330, 40, 40, "gui/btn_mute.png", self.btn_mute_click, "a", font="assets\Early GameBoy.ttf", font_size=1, font_color="whitesmoke")
        ###################

        #### AGREGO LOS CONTROLES A UNA LISTAS ####
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)
        #self.lista_widgets.append(self.btn_on_off)
        self.lista_widgets.append(self.txt_box)
        self.lista_widgets.append(self.btn_txt)


        #musica
        pygame.mixer.music.load("assets/sonidos/Pokémon Fire Red - Title Screen (HQ).mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        self.render()
    

    def render(self):
        self._slave.fill(self._color_background)
    
    #self.txtbox.get_text() obtengo el texto del txtbox

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
        return super().update(lista_eventos)

    def btn_tabla_click(self, texto):
        lista_filas = obtener_datos()
        dic_score = [{'jugador': {lista_filas[0]['nombre']}, 'Score': {lista_filas[0]['score']}},
                    {'jugador': {lista_filas[1]['nombre']}, 'Score': {lista_filas[1]['score']}},
                    {'jugador': {lista_filas[2]['nombre']}, 'Score': {lista_filas[2]['score']}}
                    ]
        
        form_puntaje = FormMenuScore(self._master, 250, 25, 500, 550, (220,0,220), "white",
                                    True, "gui/Window.png", dic_score, 100, 10, 10)
        
        self.show_dialog(form_puntaje)


    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen*100)}%")
        pygame.mixer.music.set_volume(self.volumen)
    
    
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
                                flag_home=True
                                )
        self.show_dialog(frm_jugar)

    def btn_play_click(self, param):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "chartreuse3"
            self.btn_play.set_text("Resume")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "brown3"
            self.btn_play.set_text("Pause")
            
        self.flag_play = not self.flag_play

    def btn_mute_click(self, param):
        if not self.flag_mute:
            pygame.mixer.music.pause()
            pygame.mixer.stop()
            self.flag_mute = True
        else:
            pygame.mixer.music.unpause()
            self.flag_mute = False

    def btn_guardar_nombre_click(self, param):
        user = self.txt_box.get_text()
        insertar_usuario(str(user), 0)
