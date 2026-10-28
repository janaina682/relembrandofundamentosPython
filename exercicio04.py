#exercicio 21 
import pygame

print('Exercício 21 - Tocando música')
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)