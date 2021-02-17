import pygame, sys 
from pygame.locals import * 

pygame.init()

size = width, height = 480,320
screen = pygame.display.set_mode(size)
r = 0
bif = pygame.image.load("bigmap2.png") 
pygame.display.set_caption("Pygame 2D RPG !")
x,y=0,0
CameraX, CameraY = 0, 0
movex, movey=0,0
CamX, CamY = 0,0
character="sprites\standing.png"
player=pygame.image.load(character).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type==KEYDOWN:
            if event.key==K_a:
                movex=-1
                CamX -= 1 
            elif event.key==K_d:
                movex=+1
                CamX += 1 
            elif event.key==K_w:
                movey=-1
                CamY -= 1 
            elif event.key==K_s:
                movey=+1
                CamY += 1 
        if event.type==KEYUP:        
            if event.key==K_a:
                movex=0
            elif event.key==K_d:
                movex=0
            elif event.key==K_w:
                movey=0
            elif event.key==K_s:
                movey=0    

    x+=movex
    y+=movey
    CameraX +=10
    Cameray +=10 
    print(CameraX, CameraY)
    screen.fill((r,0,0))
    screen.blit(bif,(0-CameraX,0 -CameraY))
    screen.blit(player,(x -CameraX,y -CameraY))
    pygame.display.flip()
