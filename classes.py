import pygame
win = pygame.display.set_mode((500,500))

class Camera:
    def __init(self, x, y):
        self.x
        self.y
        self.Camvel = 10
        
class Player():
    def __init__(self,x,y,height, width, health, CameraX, CameraY,varwidth,varheight):
        self.x = x
        self.y = y
        self.win = win 
        self.width = width
        self.height = height
        self.vel = 5
        self.CameraX = CameraX 
        self.CameraY = CameraY
        self.varwidth = varwidth
        self.varheight = varheight
        self.camvel = 10 
        self.inventory = []
        self.facing = 1
        self.walkCount = 0
        self.ani_count = 0
        self.hitbox = (self.x - self.CameraX, self.y - self.CameraY, self.height,self.width) 
        self.health = 50
        self.healthbar = (self.x - self.CameraX, self.y - self.CameraY, self.health, 10) 
        self.isright = False
        self.action = False 
        self.right = [pygame.image.load('manwalk/027.png'),
            pygame.image.load('manwalk/028.png'),
            pygame.image.load('manwalk/029.png'),
            pygame.image.load('manwalk/030.png'),
            pygame.image.load('manwalk/031.png'),
            pygame.image.load('manwalk/032.png'),
            pygame.image.load('manwalk/033.png'),
            pygame.image.load('manwalk/034.png'),
            pygame.image.load('manwalk/035.png')]
        self.isleft = False
        self.left = [
            pygame.image.load('manwalk/009.png'),
            pygame.image.load('manwalk/010.png'),
            pygame.image.load('manwalk/011.png'),
            pygame.image.load('manwalk/012.png'),
            pygame.image.load('manwalk/013.png'),
            pygame.image.load('manwalk/014.png'),
            pygame.image.load('manwalk/015.png'),
            pygame.image.load('manwalk/016.png'),
            pygame.image.load('manwalk/017.png')]
        self.isstanding = False
        self.standing = pygame.image.load('manwalk/018.png')
        self.isup = False
        self.up = [pygame.image.load('manwalk/000.png'),
            pygame.image.load('manwalk/001.png'),
            pygame.image.load('manwalk/002.png'),
            pygame.image.load('manwalk/003.png'),
            pygame.image.load('manwalk/004.png'),
            pygame.image.load('manwalk/005.png'),
            pygame.image.load('manwalk/006.png'),
            pygame.image.load('manwalk/007.png'),
            pygame.image.load('manwalk/008.png')]
        self.isdown = False
        self.down = [pygame.image.load('manwalk/018.png'),
            pygame.image.load('manwalk/019.png'),
            pygame.image.load('manwalk/020.png'),
            pygame.image.load('manwalk/021.png'),
            pygame.image.load('manwalk/022.png'),
            pygame.image.load('manwalk/023.png'),
            pygame.image.load('manwalk/024.png'),
            pygame.image.load('manwalk/025.png'),
            pygame.image.load('manwalk/026.png')]
        self.isdead = False
        self.dead = [pygame.image.load('mandie/000.png'),
            pygame.image.load('mandie/001.png'),
            pygame.image.load('mandie/002.png'),
            pygame.image.load('mandie/003.png'),
            pygame.image.load('mandie/004.png')]
        self.isrobe = True
        self.robestanding = pygame.image.load('robe/018.png')
        self.robeup = [pygame.image.load('robe/000.png'),
            pygame.image.load('robe/001.png'),
            pygame.image.load('robe/002.png'),
            pygame.image.load('robe/003.png'),
            pygame.image.load('robe/004.png'),
            pygame.image.load('robe/005.png'),
            pygame.image.load('robe/006.png'),
            pygame.image.load('robe/007.png'),
            pygame.image.load('robe/008.png')]
        self.robedown = [pygame.image.load('robe/018.png'),
            pygame.image.load('robe/019.png'),
            pygame.image.load('robe/020.png'),
            pygame.image.load('robe/021.png'),
            pygame.image.load('robe/022.png'),
            pygame.image.load('robe/023.png'),
            pygame.image.load('robe/024.png'),
            pygame.image.load('robe/025.png'),
            pygame.image.load('robe/026.png')]
        self.robert = [pygame.image.load('robe/027.png'),
            pygame.image.load('robe/028.png'),
            pygame.image.load('robe/029.png'),
            pygame.image.load('robe/030.png'),
            pygame.image.load('robe/031.png'),
            pygame.image.load('robe/032.png'),
            pygame.image.load('robe/033.png'),
            pygame.image.load('robe/034.png'),
            pygame.image.load('robe/035.png')]
        self.robelft = [pygame.image.load('robe/009.png'),
            pygame.image.load('robe/010.png'),
            pygame.image.load('robe/011.png'),
            pygame.image.load('robe/012.png'),
            pygame.image.load('robe/013.png'),
            pygame.image.load('robe/014.png'),
            pygame.image.load('robe/015.png'),
            pygame.image.load('robe/016.png'),
            pygame.image.load('robe/017.png')]
        self.robeskrt_standing = pygame.image.load('robe/robe_skirt/018.png')
        self.robeskrt_up = [pygame.image.load('robe/robe_skirt/000.png'),
            pygame.image.load('robe/robe_skirt/001.png'),
            pygame.image.load('robe/robe_skirt/002.png'),
            pygame.image.load('robe/robe_skirt/003.png'),
            pygame.image.load('robe/robe_skirt/004.png'),
            pygame.image.load('robe/robe_skirt/005.png'),
            pygame.image.load('robe/robe_skirt/006.png'),
            pygame.image.load('robe/robe_skirt/007.png'),
            pygame.image.load('robe/robe_skirt/008.png')]
        self.robeskrt_rt = [
            pygame.image.load('robe/robe_skirt/009.png'),
            pygame.image.load('robe/robe_skirt/010.png'),
            pygame.image.load('robe/robe_skirt/011.png'),
            pygame.image.load('robe/robe_skirt/012.png'),
            pygame.image.load('robe/robe_skirt/013.png'),
            pygame.image.load('robe/robe_skirt/014.png'),
            pygame.image.load('robe/robe_skirt/015.png'),
            pygame.image.load('robe/robe_skirt/016.png'),
            pygame.image.load('robe/robe_skirt/017.png')]
        self.robeskrt_down = [
pygame.image.load('robe/robe_skirt/018.png'),
pygame.image.load('robe/robe_skirt/019.png'),
pygame.image.load('robe/robe_skirt/020.png'),
pygame.image.load('robe/robe_skirt/021.png'),
pygame.image.load('robe/robe_skirt/022.png'),
pygame.image.load('robe/robe_skirt/023.png'),
pygame.image.load('robe/robe_skirt/024.png'),
pygame.image.load('robe/robe_skirt/025.png'),
pygame.image.load('robe/robe_skirt/026.png')]
        self.robeskrt_lft = [
pygame.image.load('robe/robe_skirt/027.png'),
pygame.image.load('robe/robe_skirt/028.png'),
pygame.image.load('robe/robe_skirt/029.png'),
pygame.image.load('robe/robe_skirt/030.png'),
pygame.image.load('robe/robe_skirt/031.png'),
pygame.image.load('robe/robe_skirt/032.png'),
pygame.image.load('robe/robe_skirt/033.png'),
pygame.image.load('robe/robe_skirt/034.png'),
pygame.image.load('robe/robe_skirt/035.png')]
        self.robehood_standing =pygame.image.load('robe/robe_hood/018.png')
        self.robehood_up = [
pygame.image.load('robe/robe_hood/000.png'),
pygame.image.load('robe/robe_hood/001.png'),
pygame.image.load('robe/robe_hood/002.png'),
pygame.image.load('robe/robe_hood/003.png'),
pygame.image.load('robe/robe_hood/004.png'),
pygame.image.load('robe/robe_hood/005.png'),
pygame.image.load('robe/robe_hood/006.png'),
pygame.image.load('robe/robe_hood/007.png'),
pygame.image.load('robe/robe_hood/008.png')]
        self.robehood_lft = [
pygame.image.load('robe/robe_hood/009.png'),
pygame.image.load('robe/robe_hood/010.png'),
pygame.image.load('robe/robe_hood/011.png'),
pygame.image.load('robe/robe_hood/012.png'),
pygame.image.load('robe/robe_hood/013.png'),
pygame.image.load('robe/robe_hood/014.png'),
pygame.image.load('robe/robe_hood/015.png'),
pygame.image.load('robe/robe_hood/016.png'),
pygame.image.load('robe/robe_hood/017.png')]
        self.robehood_down = [
pygame.image.load('robe/robe_hood/018.png'),
pygame.image.load('robe/robe_hood/019.png'),
pygame.image.load('robe/robe_hood/020.png'),
pygame.image.load('robe/robe_hood/021.png'),
pygame.image.load('robe/robe_hood/022.png'),
pygame.image.load('robe/robe_hood/023.png'),
pygame.image.load('robe/robe_hood/024.png'),
pygame.image.load('robe/robe_hood/025.png'),
pygame.image.load('robe/robe_hood/026.png')]
        self.robehood_rt = [
pygame.image.load('robe/robe_hood/027.png'),
pygame.image.load('robe/robe_hood/028.png'),
pygame.image.load('robe/robe_hood/029.png'),
pygame.image.load('robe/robe_hood/030.png'),
pygame.image.load('robe/robe_hood/031.png'),
pygame.image.load('robe/robe_hood/032.png'),
pygame.image.load('robe/robe_hood/033.png'),
pygame.image.load('robe/robe_hood/034.png'),
pygame.image.load('robe/robe_hood/035.png')]
        self.thrust = False
        self.thrust_up = [
pygame.image.load('manwalk/man_thrust/000.png'),
pygame.image.load('manwalk/man_thrust/001.png'),
pygame.image.load('manwalk/man_thrust/002.png'),
pygame.image.load('manwalk/man_thrust/003.png'),
pygame.image.load('manwalk/man_thrust/004.png'),
pygame.image.load('manwalk/man_thrust/005.png'),
pygame.image.load('manwalk/man_thrust/006.png'),
pygame.image.load('manwalk/man_thrust/007.png')]
        self.thrust_lft = [
pygame.image.load('manwalk/man_thrust/008.png'),
pygame.image.load('manwalk/man_thrust/009.png'),
pygame.image.load('manwalk/man_thrust/010.png'),
pygame.image.load('manwalk/man_thrust/011.png'),
pygame.image.load('manwalk/man_thrust/012.png'),
pygame.image.load('manwalk/man_thrust/013.png'),
pygame.image.load('manwalk/man_thrust/014.png'),
pygame.image.load('manwalk/man_thrust/015.png')]
        self.thrust_down = [
pygame.image.load('manwalk/man_thrust/016.png'),
pygame.image.load('manwalk/man_thrust/017.png'),
pygame.image.load('manwalk/man_thrust/018.png'),
pygame.image.load('manwalk/man_thrust/019.png'),
pygame.image.load('manwalk/man_thrust/020.png'),
pygame.image.load('manwalk/man_thrust/021.png'),
pygame.image.load('manwalk/man_thrust/022.png'),
pygame.image.load('manwalk/man_thrust/023.png')]
        self.thrust_rt = [
pygame.image.load('manwalk/man_thrust/024.png'),
pygame.image.load('manwalk/man_thrust/025.png'),
pygame.image.load('manwalk/man_thrust/026.png'),
pygame.image.load('manwalk/man_thrust/027.png'),
pygame.image.load('manwalk/man_thrust/028.png'),
pygame.image.load('manwalk/man_thrust/029.png'),
pygame.image.load('manwalk/man_thrust/030.png'),
pygame.image.load('manwalk/man_thrust/031.png')]
        self.robeskrt_thrust_up = [
pygame.image.load('robe/robe_skrt_thrust/000.png'),
pygame.image.load('robe/robe_skrt_thrust/001.png'),
pygame.image.load('robe/robe_skrt_thrust/002.png'),
pygame.image.load('robe/robe_skrt_thrust/003.png'),
pygame.image.load('robe/robe_skrt_thrust/004.png'),
pygame.image.load('robe/robe_skrt_thrust/005.png'),
pygame.image.load('robe/robe_skrt_thrust/006.png'),
pygame.image.load('robe/robe_skrt_thrust/007.png')]
        self.robeskrt_thrust_lft = [pygame.image.load('robe/robe_skrt_thrust/008.png'),
pygame.image.load('robe/robe_skrt_thrust/009.png'),
pygame.image.load('robe/robe_skrt_thrust/010.png'),
pygame.image.load('robe/robe_skrt_thrust/011.png'),
pygame.image.load('robe/robe_skrt_thrust/012.png'),
pygame.image.load('robe/robe_skrt_thrust/013.png'),
pygame.image.load('robe/robe_skrt_thrust/014.png'),
pygame.image.load('robe/robe_skrt_thrust/015.png')]
        self.robeskrt_thrust_down = [pygame.image.load('robe/robe_skrt_thrust/016.png'),
pygame.image.load('robe/robe_skrt_thrust/017.png'),
pygame.image.load('robe/robe_skrt_thrust/018.png'),
pygame.image.load('robe/robe_skrt_thrust/019.png'),
pygame.image.load('robe/robe_skrt_thrust/020.png'),
pygame.image.load('robe/robe_skrt_thrust/021.png'),
pygame.image.load('robe/robe_skrt_thrust/022.png'),
pygame.image.load('robe/robe_skrt_thrust/023.png')]
        self.robeskrt_thrust_rt = [
pygame.image.load('robe/robe_skrt_thrust/024.png'),
pygame.image.load('robe/robe_skrt_thrust/025.png'),
pygame.image.load('robe/robe_skrt_thrust/026.png'),
pygame.image.load('robe/robe_skrt_thrust/027.png'),
pygame.image.load('robe/robe_skrt_thrust/028.png'),
pygame.image.load('robe/robe_skrt_thrust/029.png'),
pygame.image.load('robe/robe_skrt_thrust/030.png'),
pygame.image.load('robe/robe_skrt_thrust/031.png')]
        self.robeshirt_thrust_up =[
pygame.image.load('robe/robe_shirt_thrust/000.png'),
pygame.image.load('robe/robe_shirt_thrust/001.png'),
pygame.image.load('robe/robe_shirt_thrust/002.png'),
pygame.image.load('robe/robe_shirt_thrust/003.png'),
pygame.image.load('robe/robe_shirt_thrust/004.png'),
pygame.image.load('robe/robe_shirt_thrust/005.png'),
pygame.image.load('robe/robe_shirt_thrust/006.png'),
pygame.image.load('robe/robe_shirt_thrust/007.png')]
        self.robeshirt_thrust_lft = [
pygame.image.load('robe/robe_shirt_thrust/008.png'),
pygame.image.load('robe/robe_shirt_thrust/009.png'),
pygame.image.load('robe/robe_shirt_thrust/010.png'),
pygame.image.load('robe/robe_shirt_thrust/011.png'),
pygame.image.load('robe/robe_shirt_thrust/012.png'),
pygame.image.load('robe/robe_shirt_thrust/013.png'),
pygame.image.load('robe/robe_shirt_thrust/014.png'),
pygame.image.load('robe/robe_shirt_thrust/015.png')]
        self.robeshirt_thrust_down =[
pygame.image.load('robe/robe_shirt_thrust/016.png'),
pygame.image.load('robe/robe_shirt_thrust/017.png'),
pygame.image.load('robe/robe_shirt_thrust/018.png'),
pygame.image.load('robe/robe_shirt_thrust/019.png'),
pygame.image.load('robe/robe_shirt_thrust/020.png'),
pygame.image.load('robe/robe_shirt_thrust/021.png'),
pygame.image.load('robe/robe_shirt_thrust/022.png'),
pygame.image.load('robe/robe_shirt_thrust/023.png')]
        self.robeshirt_thrust_rt = [
pygame.image.load('robe/robe_shirt_thrust/024.png'),
pygame.image.load('robe/robe_shirt_thrust/025.png'),
pygame.image.load('robe/robe_shirt_thrust/026.png'),
pygame.image.load('robe/robe_shirt_thrust/027.png'),
pygame.image.load('robe/robe_shirt_thrust/028.png'),
pygame.image.load('robe/robe_shirt_thrust/029.png'),
pygame.image.load('robe/robe_shirt_thrust/030.png'),
pygame.image.load('robe/robe_shirt_thrust/031.png')]     
        self.robe_hood_thrust_up=[
            pygame.image.load('robe/robe_hood_thrust/000.png'),
pygame.image.load('robe/robe_hood_thrust/001.png'),
pygame.image.load('robe/robe_hood_thrust/002.png'),
pygame.image.load('robe/robe_hood_thrust/003.png'),
pygame.image.load('robe/robe_hood_thrust/004.png'),
pygame.image.load('robe/robe_hood_thrust/005.png'),
pygame.image.load('robe/robe_hood_thrust/006.png'),
pygame.image.load('robe/robe_hood_thrust/007.png')]
        self.robe_hood_thrust_lft=[
pygame.image.load('robe/robe_hood_thrust/008.png'),
pygame.image.load('robe/robe_hood_thrust/009.png'),
pygame.image.load('robe/robe_hood_thrust/010.png'),
pygame.image.load('robe/robe_hood_thrust/011.png'),
pygame.image.load('robe/robe_hood_thrust/012.png'),
pygame.image.load('robe/robe_hood_thrust/013.png'),
pygame.image.load('robe/robe_hood_thrust/014.png'),
pygame.image.load('robe/robe_hood_thrust/015.png')]
        self.robe_hood_thrust_down=[
pygame.image.load('robe/robe_hood_thrust/016.png'),
pygame.image.load('robe/robe_hood_thrust/017.png'),
pygame.image.load('robe/robe_hood_thrust/018.png'),
pygame.image.load('robe/robe_hood_thrust/019.png'),
pygame.image.load('robe/robe_hood_thrust/020.png'),
pygame.image.load('robe/robe_hood_thrust/021.png'),
pygame.image.load('robe/robe_hood_thrust/022.png'),
pygame.image.load('robe/robe_hood_thrust/023.png')]
        self.robe_hood_thrust_rt= [
pygame.image.load('robe/robe_hood_thrust/024.png'),
pygame.image.load('robe/robe_hood_thrust/025.png'),
pygame.image.load('robe/robe_hood_thrust/026.png'),
pygame.image.load('robe/robe_hood_thrust/027.png'),
pygame.image.load('robe/robe_hood_thrust/028.png'),
pygame.image.load('robe/robe_hood_thrust/029.png'),
pygame.image.load('robe/robe_hood_thrust/030.png'),
pygame.image.load('robe/robe_hood_thrust/031.png')]
        self.weapon_staff = True
        self.staff_thrust_up =[pygame.image.load('weapon/staff_thrust/000.png'),
pygame.image.load('weapon/staff_thrust/001.png'),
pygame.image.load('weapon/staff_thrust/002.png'),
pygame.image.load('weapon/staff_thrust/003.png'),
pygame.image.load('weapon/staff_thrust/004.png'),
pygame.image.load('weapon/staff_thrust/005.png'),
pygame.image.load('weapon/staff_thrust/006.png'),
pygame.image.load('weapon/staff_thrust/007.png')]
        self.staff_thrust_lft = [pygame.image.load('weapon/staff_thrust/008.png'),
pygame.image.load('weapon/staff_thrust/009.png'),
pygame.image.load('weapon/staff_thrust/010.png'),
pygame.image.load('weapon/staff_thrust/011.png'),
pygame.image.load('weapon/staff_thrust/012.png'),
pygame.image.load('weapon/staff_thrust/013.png'),
pygame.image.load('weapon/staff_thrust/014.png'),
pygame.image.load('weapon/staff_thrust/015.png')]
        self.staff_thrust_down = [pygame.image.load('weapon/staff_thrust/016.png'),
pygame.image.load('weapon/staff_thrust/017.png'),
pygame.image.load('weapon/staff_thrust/018.png'),
pygame.image.load('weapon/staff_thrust/019.png'),
pygame.image.load('weapon/staff_thrust/020.png'),
pygame.image.load('weapon/staff_thrust/021.png'),
pygame.image.load('weapon/staff_thrust/022.png'),
pygame.image.load('weapon/staff_thrust/023.png')]
        self.staff_thrust_rt = [
            pygame.image.load('weapon/staff_thrust/024.png'),
pygame.image.load('weapon/staff_thrust/025.png'),
pygame.image.load('weapon/staff_thrust/026.png'),
pygame.image.load('weapon/staff_thrust/027.png'),
pygame.image.load('weapon/staff_thrust/028.png'),
pygame.image.load('weapon/staff_thrust/029.png'),
pygame.image.load('weapon/staff_thrust/030.png'),
pygame.image.load('weapon/staff_thrust/031.png')]

        self.chain_helm_up = [
                          pygame.image.load('chain/chain_helm/000.png'),
                          pygame.image.load('chain/chain_helm/001.png'),
                          pygame.image.load('chain/chain_helm/002.png'),
                          pygame.image.load('chain/chain_helm/003.png'),
                          pygame.image.load('chain/chain_helm/004.png'),
                          pygame.image.load('chain/chain_helm/005.png'),
                          pygame.image.load('chain/chain_helm/006.png'),
                          pygame.image.load('chain/chain_helm/007.png'),
                          pygame.image.load('chain/chain_helm/008.png')]

        self.chain_helm_lft = [
                           pygame.image.load('chain/chain_helm/009.png'),
                           pygame.image.load('chain/chain_helm/010.png'),
                           pygame.image.load('chain/chain_helm/011.png'),
                           pygame.image.load('chain/chain_helm/012.png'),
                           pygame.image.load('chain/chain_helm/013.png'),
                           pygame.image.load('chain/chain_helm/014.png'),
                           pygame.image.load('chain/chain_helm/015.png'),
                           pygame.image.load('chain/chain_helm/016.png'),
                           pygame.image.load('chain/chain_helm/017.png')]
        self.chain_helm_down = [

                            pygame.image.load('chain/chain_helm/018.png'),
                            pygame.image.load('chain/chain_helm/019.png'),
                            pygame.image.load('chain/chain_helm/020.png'),
                            pygame.image.load('chain/chain_helm/021.png'),
                            pygame.image.load('chain/chain_helm/022.png'),
                            pygame.image.load('chain/chain_helm/023.png'),
                            pygame.image.load('chain/chain_helm/024.png'),
                            pygame.image.load('chain/chain_helm/025.png'),
                            pygame.image.load('chain/chain_helm/026.png')
                            ]

        self.chain_helm_rt = [
                    pygame.image.load('chain/chain_helm/027.png'),
                    pygame.image.load('chain/chain_helm/028.png'),
                    pygame.image.load('chain/chain_helm/029.png'),
                    pygame.image.load('chain/chain_helm/030.png'),
                    pygame.image.load('chain/chain_helm/031.png'),
                    pygame.image.load('chain/chain_helm/032.png'),
                    pygame.image.load('chain/chain_helm/033.png'),
                    pygame.image.load('chain/chain_helm/034.png'),
                    pygame.image.load('chain/chain_helm/035.png')]
        
        self.chain_helm_standing = pygame.image.load('chain/chain_helm/018.png')
        self.ischain = True
        self.ischain_helm = True


    def hit(self):
        if self.health > 0:
            print('HIT')
            self.health -= 20
        elif self.health <= 0:
            print('DEAD DEAD DEAD')
            self.isdead = True
            self.isstanding = False
            self.isright = False
            self.isleft = False
            self.isup = False
            self.isdown = False
            self.action = False
            if self.isdead:
                win.blit(self.dead[round(self.ani_count)], (self.x - self.CameraX, self.y - self.CameraY))



    def draw(self, win):
        self.healthbar
        self.hitbox
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        pygame.draw.rect(win,(255,0,0),self.healthbar,0)
        if self.isstanding:
            win.blit(self.standing, (self.x - self.CameraX, self.y - self.CameraY))

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.ani_count + 1 >=17:
            self.ani_count = 0

        if self.isleft:
            self.walkCount += 1
            win.blit(self.left[round(self.walkCount//3)], (self.x - self.CameraX, self.y - self.CameraY))
            self.facing = -1

        if self.isright:
            self.facing = 1
            win.blit(self.right[round(self.walkCount//3)], (self.x-self.CameraX,self.y-self.CameraY))
            self.walkCount +=1

        if self.isup:
            self.walkCount +=1
            win.blit(self.up[round(self.walkCount//3)], (self.x - self.CameraX, self.y - self.CameraY))
            self.facing = -2
        if self.isdown:
            self.walkCount +=1
            win.blit(self.down[round(self.walkCount//3)], (self.x - self.CameraX, self.y - self.CameraY))
            self.facing = 2

        if self.ischain:
            
            if self.isstanding:
                win.blit(self.chain_helm_standing, (self.x - self.CameraX, self.y - self.CameraY))
            if self.isup:
                win.blit(self.chain_helm_up[self.walkCount//3], (self.x - self.CameraX, self.y - self.CameraY))
            if self.isdown:
                    win.blit(self.chain_helm_down[self.walkCount//3], (self.x - self.CameraX, self.y - self.CameraY))
            if self.isright:
                    win.blit(self.chain_helm_rt[self.walkCount//3], (self.x - self.CameraX, self.y - self.CameraY))
            if self.isleft:
                    win.blit(self.chain_helm_lft[self.walkCount//3], (self.x - self.CameraX, self.y - self.CameraY))

        if self.isrobe:
            if self.isstanding:
                win.blit(self.robestanding, (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robeskrt_standing,
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robehood_standing,
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
            if self.isup:
                win.blit(self.robeup[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robeskrt_up[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robehood_up[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
            if self.isdown:
                win.blit(self.robedown[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robeskrt_down[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robehood_down[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
            if self.isright:
                win.blit(self.robeskrt_rt[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robert[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robehood_rt[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
            if self.isleft:
                win.blit(self.robeskrt_lft[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robehood_lft[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                win.blit(self.robelft[round(self.walkCount // 3)],
                         (round(self.x - self.CameraX), round(self.y - self.CameraY)))

        if self.action: #thrust rights

            self.ani_count += 1

            if self.weapon_staff:
                
                if self.facing == 1:
                    win.blit(self.thrust_rt[round(self.ani_count // 3)], (self.x - self.CameraX, self.y - self.CameraY))
                    win.blit(self.robeskrt_thrust_rt[round(self.ani_count // 3)], (self.x - self.CameraX, self.y - self.CameraY))
                    win.blit(self.robeshirt_thrust_rt[round(self.ani_count // 3)],(self.x - self.CameraX, self.y - self.CameraY))
                    win.blit(self.robe_hood_thrust_rt[round(self.ani_count//3)], (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                    if self.weapon_staff:
                        win.blit(self.staff_thrust_rt[round(self.ani_count//3)], (round(self.x - self.CameraX), round(self.y - self.CameraY)))


                if self.facing == -1:
                    win.blit(self.thrust_lft[round(self.ani_count // 3)], (self.x - self.CameraX, self.y - self.CameraY))
                    win.blit(self.robeskrt_thrust_lft[round(self.ani_count // 3)], (self.x - self.CameraX, self.y - self.CameraY))
                    win.blit(self.robeshirt_thrust_lft[round(self.ani_count // 3)],(self.x - self.CameraX, self.y - self.CameraY))
                    win.blit(self.robe_hood_thrust_lft[round(self.ani_count//3)], (round(self.x - self.CameraX), round(self.y - self.CameraY)))
                    if self.weapon_staff:
                        win.blit(self.staff_thrust_lft[round(self.ani_count//3)], (round(self.x - self.CameraX), round(self.y - self.CameraY)))

        








       
class Map():
    def  __init__(self,x,y,CameraX,CameraY,varwidth, varheight):
        self.x = x
        self.y = y
        self.cam = self.Camera()
        self.win = win
        self.vel= 5
        self.pic= pygame.image.load('bigmap2.png')
        self.CameraX = CameraX
        self.CameraY = CameraY
        self.varwidth = varwidth
        self.varheight = varheight
        self.camvel = 10 



   

    class Camera:
        def __init(self, x, y):
            self.x
            self.y
            self.Camvel = 10

    def draw(self, win):
        win.blit(self.pic, (self.x - self.CameraX , self.y - self.CameraY))
        
