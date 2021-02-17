import pygame
from classes import *
from NPC import *
#import text
pygame.font.init()

pygame.init()
pygame.font.init()



winheight = 600
winwidth = 800

win = pygame.display.set_mode((winwidth, winheight))


pygame.display.set_caption("Ben's Game")
bg = pygame.image.load("bigmap2.png")

x = 50
y = 50
width = 40
height = 60
vel = 5
CameraX = 0
CameraY = 0
clock = pygame.time.Clock()


    
run = True
player = Player(winwidth/2, winheight/2 ,64,64,50,0,0,width,height)
maps = Map(0,0,0,0,width, height)
guy = NPC_Man(20, 20,64,64,50,0,0,width,height)
robe = pygame.image.load('robe/018.png')

player.isrobe = True




myfont = pygame.font.SysFont('fixedsys',30)
textsurface = myfont.render('', True, (0,0,0))


while run:
    #print(player.walkCount)
    clock.tick(27)
    win.fill((0,0,0))
    if player.x < 50:
        textsurface = myfont.render('hello I am Tyler Im in the corner like my robes', True, (0, 0, 0))
        if guy.isdead:
            textsurface = myfont.render('OUCH!', True, (0, 0, 0))
    maps.draw(win)
    player.draw(win)
    guy.draw(win)
    pygame.draw.rect(win, (255, 255, 255), (0,500,800,100), 0)
    win.blit(textsurface, (0, 500))


    #print('guy',guy.hitbox[0],guy.hitbox[1],guy.hitbox[2],guy.hitbox[3],'Player',player.hitbox[0], player.hitbox[1],player.hitbox[2],player.hitbox[3])
    #print(player.facing)
    #player.hitbox [1]
    # if facing is (-)  left, if facing is (+) right
    # if the player.hitbox[0] - 32 (is on the left then hitbox[0]
    #if player.hitbox[1]

    if (player.hitbox[0] <= (guy.hitbox[0] + 64)) and (player.hitbox[1] <= guy.hitbox[1]+64):
        #print('inside!')
        if player.action:
            print('BONK')
            guy.hit()
            
    player.hitbox = (player.x - player.CameraX, player.y - player.CameraY, player.height,player.width)
    player.healthbar = (player.x - player.CameraX, player.y - player.CameraY, player.health, 10)
    
    #guy.hitbox = (guy.x - guy.CameraX, guy.y - guy.CameraY, guy.health, guy.height, guy.width)
    #guy.healtbar = (guy.x - guy.CameraX, guy.y - guy.CameraY, guy.health, 10)
    #win.blit(guy.healthbar, (guy.x - guy.CameraX, guy.y - guy.CameraY, guy.health, 10) )


    
    if player.isrobe:
        if player.isstanding:
            win.blit(player.robestanding, (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robeskrt_standing, (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robehood_standing, (round(player.x - player.CameraX), round(player.y - player.CameraY)))
        if player.isup:
            win.blit(player.robeup[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robeskrt_up[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robehood_up[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
        if player.isdown:
            win.blit(player.robedown[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robeskrt_down[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robehood_down[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
        if player.isright:
            win.blit(player.robeskrt_rt[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robert[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robehood_rt[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
        if player.isleft:

            win.blit(player.robeskrt_lft[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robehood_lft[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))
            win.blit(player.robelft[round(player.walkCount//3)], (round(player.x - player.CameraX), round(player.y - player.CameraY)))

    if player.x == 0 and player.y ==0:
        player.hit()
        
    if player.isdead:
        pass
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys != pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_down:
            player.isstanding = True
            player.isright = False
            player.isleft = False
            player.isdown = False
            player.isup = False
            
    if keys[pygame.K_LEFT]:

        if player.x == 0:
            pass

        else:
            player.x -= vel


        if player.x - winwidth/2 <= 0:
            pass
        elif player.x + winwidth/2 >= 1595:
            pass
        else:
            player.CameraX -= vel
            maps.CameraX -= vel
            guy.CameraX -= vel



        player.isstanding = False
        player.isright = False
        player.isleft = True
        player.isup = False
        player.isdown = False

   

    if keys[pygame.K_RIGHT]:
        # new instance starts at 1595
        # map ends at 2645
        # want him to stop at 1470
        if player.x >= 2645:
            pass
        elif player.x >= 1520:
            pass
        else:
            player.x += vel   

        if player.x - winwidth/2 < 0:
            pass
        elif player.x + winwidth/2 >= 2645:
            pass
        elif player.x + winwidth/2 >= 1595:
            pass
        else:
            player.CameraX += vel
            maps.CameraX += vel
            guy.CameraX += vel



        player.isstanding = False
        player.isright = True
        player.isleft = False
        player.isup = False
        player.isdown = False

        
    if keys[pygame.K_UP]:
        
        player.isstanding = False
        player.isright = False
        player.isleft = False
        player.isdown = False
        player.isup = True
        
        if player.y == 0:
            pass
        else:
            player.y -= vel            


        if player.y < winheight/2:
            pass
        elif player.y + winheight/2 >= 2400 :
            pass
        else:
            player.CameraY -= vel
            maps.CameraY -= vel
            guy.CameraY -= vel



            

        
    if keys[pygame.K_DOWN]:
        
        player.isstanding = False
        player.isright = False
        player.isleft = False
        player.isup = False
        player.isdown = True


        # if player moves out of bounds they can move in and then out again

        if player.y >= 2230: # Stops the Player
            print('NO STOP')
            pass
        elif  player.y + winheight/2 <= player.CameraY:
            print('player.y + half the screen width > the Camera!')
        else:
            player.y += vel


        if player.y + winheight/2 >= 2400 : #Stops the Screen
            pass
        elif player.y < winheight/2:
            pass
        else:
            player.CameraY += vel
            maps.CameraY += vel
            guy.CameraY += vel




        player.isstanding = False
        player.isright = False
        player.isleft = False
        player.isup = False
        player.isdown = True

    if keys[pygame.K_SPACE]:
        #print('its SPACE')
        player.isstanding = False
        player.isright = False
        player.isleft = False
        player.isup = False
        player.isdown = False
        player.action = True
    else:
        player.action = False
        if keys[pygame.K_SPACE]:
                if player.thrust:
                    player.isstanding = False
                    player.isright = False
                    player.isleft = False
                    player.isup = False
                    player.isdown = False
                    if guy.isdead:
                        win.blit(guy.dead[player.ani_count // 3], (guy.x - guy.CameraX, guy.y - guy.CameraY))
        else:
            player.action = False

    #guy.CameraX = 220
    #guy.CameraY = 220



    # print('player |', player.x, player.y,'| pcam x,y |' ,player.CameraX, player.CameraY,'maps', maps.x,maps.y,'mapcam x y', maps.CameraX,maps.CameraY)
    # need to make the guy.x - maps.x...
                    
    #print(player.x, winheight/2, player.x - winwidth/2, winwidth/2)


    # print(player.CameraY, player.y+winheight/2) #ends at y = 2400
    print(player.x, winheight/2)



    pygame.display.flip()
    
pygame.quit()
