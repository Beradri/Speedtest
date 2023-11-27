import pygame
from pygame.locals import *
import random
import sys

# Inicializamos Pygame
pygame.init()

# Configuración de la pantalla
ancho_pantalla = 1920
alto_pantalla = 1080
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

#Cargar imágenes
fondo = pygame.image.load("fondo.jpg").convert_alpha()

#Posiciones
Pos_semaforo = (33,0) #El 33 es temporal hasta hacer los cálculos necesarios para determinar la posición ok?

#Constantes

