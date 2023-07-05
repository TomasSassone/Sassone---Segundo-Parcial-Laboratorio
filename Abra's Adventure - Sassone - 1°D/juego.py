from classes.class_nivel_1 import *
from classes.class_nivel_2 import *
from classes.class_nivel_3 import *

def juego(pantalla, lista_eventos, nivel:int):
    match nivel:
        case 1:
            nivel_actual = Nivel_1(pantalla)
        case 2:
            nivel_actual = Nivel_2(pantalla)
        case 3:
            nivel_actual = Nivel_3(pantalla)
    nivel_actual.update(lista_eventos)