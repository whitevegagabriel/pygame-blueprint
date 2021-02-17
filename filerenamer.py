import os

##print('hello \t im ben')

q = 'if '
self = 'self.'
colon = ':'
isstand = 'isstanding'
isup = 'isup'
isdown = 'isdown'
isright = 'isright'
isleft = 'isleft'

checks = [isstand, isup, isdown, isright, isleft]  # this should be the action or item to blit
display0 = 'win.blit('

path_basic = ''
# Edit HERE

style_folder = 'chain' + '/'

# EDIT HERE

paths_plus = 'chain_helm'

paths = path_basic + style_folder + paths_plus + '/'
paths2 = path_basic + 'text' + '/' + paths_plus + '.txt'
oldname = 'tile'

filetype = '.png'

x = 0

files = 36
div = files / 4

pop = list()

while x != files:
    pop.append(x)
    x += 1
# print(pop)

x = 0

pyg = "pygame.image.load('"
f = open(paths2, 'w')

for char in pop:
    print(x)
    if x < 10:
        imager = str(pop[x])
        comb = paths + oldname + '00' + imager + filetype
        combpy = pyg + paths + '00' + imager + filetype + "'" + ")" + ","
        combnew = paths + '00' + imager + filetype

        if x == 0:
            combpy = self + paths_plus + '_up' '=' + '[' + pyg + paths + '00' + imager + filetype + "'" + ")" + ","
        if x == 7:
            combpy = pyg + paths + '00' + imager + filetype + "'" + ")" + "]"
        if x == 8:
            combpy = self + paths_plus + '_lft' '=' + '[' + pyg + paths + '00' + imager + filetype + "'" + ")" + ","
        x += 1
    elif x >= 10:
        imager = str(pop[x])
        combpy = pyg + paths + '0' + imager + filetype + "'" + ")" + ","
        comb = paths + oldname + '0' + imager + filetype
        combnew = paths + '0' + imager + filetype
        if x == 15:
            combpy = pyg + paths + '0' + imager + filetype + "'" + ")" + "]"
        if x == 16:
            combpy = self + paths_plus + '_down' '=' + '[' + pyg + paths + '0' + imager + filetype + "'" + ")" + ","
        if x == 23:
            combpy = pyg + paths + '0' + imager + filetype + "'" + ")" + "]"
        if x == 24:
            combpy = self + paths_plus + '_rt' '=' + '[' + pyg + paths + '0' + imager + filetype + "'" + ")" + "]"
        x += 1

    # print(combpy)
    print(comb)
    print(combnew)
    os.rename(comb, combnew)
    f.write(combpy)
    f.write('\n')

textpath = 'text'

t = [0, 1, 2, 3]
tt = [0, 1, 2, 3, 4]
up = 'up'
lft = 'lft'
down = 'down'
rt = 'rt'
stand = 'standing'
direction = [up, lft, down, rt, stand]

# IF then blits, Next step is to combine multiple files to write out things like hood, shirt, pants ect.

for num in tt:
    if_status = q + self + checks[num] + colon
    if checks[num] == isup:
        blits = '\n' + '\t' + display0 + self + paths_plus + '_' + direction[
            0] + ', (' + self + 'x - ' + self + 'CameraX, ' + self + 'y - ' + self + 'CameraY))' + '\n'
    elif checks[num] == isleft:
        blits = '\n' + '\t' + display0 + self + paths_plus + '_' + direction[
            1] + ', (' + self + 'x - ' + self + 'CameraX, ' + self + 'y - ' + self + 'CameraY))' + '\n'
    elif checks[num] == isdown:
        blits = '\n' + '\t' + display0 + self + paths_plus + '_' + direction[
            2] + ', (' + self + 'x - ' + self + 'CameraX, ' + self + 'y - ' + self + 'CameraY))' + '\n'
    elif checks[num] == isright:
        blits = '\n' + '\t' + display0 + self + paths_plus + '_' + direction[
            3] + ', (' + self + 'x - ' + self + 'CameraX, ' + self + 'y - ' + self + 'CameraY))' + '\n'
    elif checks[num] == isstand:
        blits = '\n' + '\t' + display0 + self + paths_plus + '_' + direction[
            4] + ', (' + self + 'x - ' + self + 'CameraX, ' + self + 'y - ' + self + 'CameraY))' + '\n'

    # print(if_status,blits)
    f.write(if_status)
    f.write(blits)

    # BLIT

# up lft down rt
# win.blit(self.doing_wearing_lft[self.Walkcount //3], (self.x - self.CameraX, self.y - self.CameraY))
for num in t:
    blits = display0 + self + paths_plus + '_' + direction[
        num] + ', (' + self + 'x - ' + self + 'CameraX, ' + self + 'y - ' + self + 'CameraY))'
    # print(blits)

f.close()


