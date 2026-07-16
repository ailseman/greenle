import pygame
import os
folder = os.path.dirname(__file__)
backgroundimg = pygame.image.load(os.path.join(folder,"background.png"))
startbutton = pygame.image.load(os.path.join(folder,"start_button.png"))
titletext = pygame.image.load(os.path.join(folder,"titletext.png"))
shuflemodebutton = pygame.image.load(os.path.join(folder,"shuflemodebutton.png"))
clasicmodebutton = pygame.image.load(os.path.join(folder,"clasicmodebutton.png"))