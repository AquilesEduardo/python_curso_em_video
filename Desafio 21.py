'''import pygame
pygame.init()
pygame.mixer.music.load('caribe.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()'''

from pygame import mixer

mixer.init()

mixer.music.load('caribe.mp3')

mixer.music.play()

import time

time.sleep(360)

__________________

from pygame import mixer

mixer.init()

mixer.music.load('caribe.mp3')

mixer.music.play()

parar = input('Digite algo para parar...')