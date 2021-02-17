import pygame
import start
import classes
pygame.font.init()
win = pygame.display.set_mode((500,500))

winheight = 600
winwidth = 800

myfont = pygame.font.SysFont('fixedsys',30)
textsurface = myfont.render('Some Text', False, (0,0,0))
win.blit(textsurface,(100,100))