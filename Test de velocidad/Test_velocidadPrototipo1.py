import pygame
from pygame.locals import *
import random
import sys
import time

# Inicializamos Pygame
pygame.init()

# Configuración de la pantalla
ancho_pantalla = 1920
alto_pantalla = 1080
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

#Cargar imágenes
fondo = pygame.image.load("fondo.jpg").convert_alpha()
semaforo = pygame.image.load("semaforo.jpg").convert_alpha()
semaforo1 = pygame.image.load("semaforo1.jpg").convert_alpha()
semaforo2 = pygame.image.load("semaforo2.jpg").convert_alpha()
semaforo3 = pygame.image.load("semaforo3.jpg").convert_alpha()
semaforo4 = pygame.image.load("semaforo4.jpg").convert_alpha()
semaforo5 = pygame.image.load("semaforo5.jpg").convert_alpha()

#Iniciar variables
contador = 0


#Constantes
font_cronometro = pygame.font.Font('freesansbold.ttf', 32)
pos_semaforo = (210, 145)
pos_fondo = (0, 0)

Funcionando = True
tiempo_inicio = pygame.time.get_ticks()

#Bucle principal
while Funcionando:
    pantalla.blit(fondo, pos_fondo)
    pantalla.blit(semaforo1, pos_semaforo)
    pygame.display.flip()
    time.sleep(1)
    pantalla.blit(semaforo2, pos_semaforo)
    pygame.display.flip()
    time.sleep(1)
    pantalla.blit(semaforo3, pos_semaforo)
    pygame.display.flip()
    time.sleep(1)
    pantalla.blit(semaforo4, pos_semaforo)
    pygame.display.flip()
    time.sleep(1)
    pantalla.blit(semaforo5, pos_semaforo)
    pygame.display.flip()
    time.sleep(1)
    pantalla.blit(semaforo, pos_semaforo)
    pygame.display.flip()
    
for evento in pygame.event.get():
    if evento.type == MOUSEBUTTONDOWN:
        tiempo_final = pygame.time.get_ticks() - tiempo_inicio
        tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) / 1000
        cronometro_texto = f"Tiempo: {tiempo_transcurrido:.3f} s"
        text_cronometro = font_cronometro.render(cronometro_texto, True, (0, 0, 0))
        text_rect_cronometro = text_cronometro.get_rect(center=(ancho_pantalla // 2, alto_pantalla + 50))
        pantalla.blit(text_cronometro, text_rect_cronometro)

    
    


pygame.quit()



