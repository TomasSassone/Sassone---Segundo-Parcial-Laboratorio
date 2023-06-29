import pygame
from configuraciones import obtener_rectangulos

class Plataforma:
    def __init__(self, left, top, width, height, surf, pantalla):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.surf = surf
        self.pantalla = pantalla
    
    
