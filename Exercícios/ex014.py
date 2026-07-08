# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame # .\.venv\Scripts\python.exe -m pip install pygame
import time

pygame.init()
pygame.mixer.music.load('Exercícios/musica.mp3') # encontrando o local do arquivo mp3
pygame.mixer.music.play() # tocando de fato

# impede que o programa termine imediatamente
while pygame.mixer.music.get_busy(): # enquanto a musica estiver tocando..
    time.sleep(0.1) # verifica se a musica acabou, se tiver acabado (True) o while interrompe