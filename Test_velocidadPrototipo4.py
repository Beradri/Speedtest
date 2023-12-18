import pygame
from pygame.locals import *
import sys
import time

# Inicializamos Pygame
pygame.init()

# Configuración de la pantalla
ancho_pantalla = 1920
alto_pantalla = 1080
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Cargar imágenes
fondo = pygame.image.load("fondo.jpg").convert_alpha()
semaforo = pygame.image.load("semaforo.jpg").convert_alpha()
semaforo1 = pygame.image.load("semaforo1.jpg").convert_alpha()
semaforo2 = pygame.image.load("semaforo2.jpg").convert_alpha()
semaforo3 = pygame.image.load("semaforo3.jpg").convert_alpha()
semaforo4 = pygame.image.load("semaforo4.jpg").convert_alpha()
semaforo5 = pygame.image.load("semaforo5.jpg").convert_alpha()

# Iniciar variables
contador = 0

# Constantes
font_cronometro = pygame.font.Font('freesansbold.ttf', 32)
pos_semaforo = (210, 145)
pos_fondo = (0, 0)

# Funciones auxiliares
def mostrar_cronometro(tiempo_transcurrido):
    cronometro_texto = f"Tiempo: {tiempo_transcurrido:.3f} s"
    text_cronometro = font_cronometro.render(cronometro_texto, True, (0, 0, 0))
    text_rect_cronometro = text_cronometro.get_rect(center=(ancho_pantalla // 2, alto_pantalla - 50))
    pantalla.blit(text_cronometro, text_rect_cronometro)
    pygame.display.flip()

# Bucle principal
Funcionando = True
tiempo_inicio = 0
tiempo_transcurrido = 0
cronometro_activo = False

while Funcionando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            Funcionando = False

    pantalla.blit(fondo, pos_fondo)
    pygame.display.flip()
    time.sleep(1)

    Imagenes = True

    while Imagenes:
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
        tiempo_inicio = pygame.time.get_ticks()
        cronometro_activo = True
        Imagenes = False

    pygame.display.flip()
    contador += 1

    if cronometro_activo:
        while cronometro_activo:
            tiempo_actual = pygame.time.get_ticks() - tiempo_inicio
            tiempo_transcurrido = tiempo_actual / 1000
            mostrar_cronometro(tiempo_transcurrido)

            for evento in pygame.event.get():
                if evento.type == MOUSEBUTTONDOWN and cronometro_activo:
                    cronometro_activo = False
                    tiempo_final = pygame.time.get_ticks() - tiempo_inicio
                    tiempo_transcurrido = tiempo_final / 1000
                    mostrar_cronometro(tiempo_transcurrido)
                    pygame.time.wait(3000)  # Esperar 3 segundos antes de cerrar el programa
                    Funcionando = False


pygame.quit()
sys.exit()

#Arreglar error