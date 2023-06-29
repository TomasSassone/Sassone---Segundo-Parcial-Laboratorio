import pygame
from pygame.locals import *

from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *
from GUI_form_menu_score import *

class FormPrueba(Form):
    def __init__(self, pantalla, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(pantalla, x, y, w, h, color_background, color_border, border_size, active)
        #volumen y mixer
        self.volumen = 0.1
        self.flag_play = True
        pygame.mixer.init()
        #### CONTROLES ####
        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "ivory3", "ivory2", "green", "hotpink", 3, font="assets\Early GameBoy.ttf", font_size = 15, font_color = "black")
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "blueviolet", "green", self.btn_play_click, "Nombre", "Pausa", font="assets\Early GameBoy.ttf", font_size=15, font_color="whitesmoke")
        self.label_volumen = Label(self._slave, 650, 190, 100, 50, "10", "assets\Early GameBoy.ttf", 15,"whitesmoke", "gui/Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "blue", "white")
        self.btn_tabla = Button_Image(self._slave, x, y, 255, 100, 50, 50, "gui/Menu_BTN.png", self.btn_tabla_click, "x")

        self.btn_lv1 = Button(self._slave, x, y, 180, 270, 150, 50, "cadetblue2", "green", self.btn_lvl1, "Nombre",
                                "Nivel 1", font="assets\Early GameBoy.ttf", font_size=15, font_color="whitesmoke")
        
        self.btn_lv2 = Button(self._slave, x, y, 380, 270, 150, 50, "cadetblue2", "green", self.btn_lvl2, "Nombre",
                                "Nivel 2", font="assets\Early GameBoy.ttf", font_size=15, font_color="whitesmoke")
        
        self.btn_lv3 = Button(self._slave, x, y, 580, 270, 150, 50, "cadetblue2", "green", self.btn_lvl3, "Nombre",
                                "Nivel 3", font="assets\Early GameBoy.ttf", font_size=15, font_color="whitesmoke")




        ###################

        #### AGREGO LOS CONTROLES A UNA LISTAS ####
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_lv1)
        self.lista_widgets.append(self.btn_lv2)
        self.lista_widgets.append(self.btn_lv3)


        #musica
        pygame.mixer.music.load("assets/Pokémon Fire Red - Title Screen (HQ).mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()
    
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

    def render(self):
        self._slave.fill(self._color_background)
    
    #self.txtbox.get_text() obtengo el texto del txtbox

    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "brown3"
            self.btn_play.set_text("Resume")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "blueviolet"
            self.btn_play.set_text("Pause")
            
        self.flag_play = not self.flag_play

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen*100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, texto):
        dic_score = [{'jugador': 'Gio', 'Score': 150},
                    {'jugador': 'Nisman', 'Score': 1000},
                    {'jugador': 'Starlord', 'Score': 350}
                    ]
        
        form_puntaje = FormMenuScore(self._master, 250, 25, 500, 550, (220,0,220), "white",
                                    True, "gui/Window.png", dic_score, 100, 10, 10)
        
        self.show_dialog(form_puntaje)
    
    def btn_lvl1(self, texto):
        pass
        #nivel_1(True)
        #self.end_dialog()

    def btn_lvl2(self, texto):
        pass
        #nivel_2(True)
        #self.end_dialog()

    def btn_lvl3(self, texto):
        pass
        #nivel_3(True)
        #self.end_dialog()