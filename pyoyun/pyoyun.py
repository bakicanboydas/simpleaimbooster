import sys,random,time,math,os
x = 500
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
import pygame
pygame.init()

#####WINDOW#########

width = 780
height = 780
boyut = (width,height)
pencere = pygame.display.set_mode(boyut)
color = pygame.Color(0,0,0)

#####MOUSE##########

aim = pygame.image.load("aim.png")
aim = pygame.transform.scale(aim , (60,60))
pygame.mouse.set_visible(False)
aimx = aim.get_size()[0]
aimy = aim.get_size()[1]


heart = pygame.image.load("heart.png")
heart = pygame.transform.scale(heart, (40,40))
heartx = heart.get_size()[0]
hearty = heart.get_size()[1]

broke_heart = pygame.image.load("broke_heart.png")
broke_heart = pygame.transform.scale(broke_heart, (50,40))
broke_heartx = heart.get_size()[0]
broke_hearty = heart.get_size()[1]


#####CLOCK##########

clock = pygame.time.Clock()

time = pygame.time.get_ticks()
fontTime = pygame.font.SysFont("ArcadeClassic",200)
time_minute = 0
#####SPRITES########

all_sprites = pygame.sprite.Group()

#####TARGET#########
target_width = 30
target_height = 30

font = pygame.font.SysFont("Helvetica",200)
skor=0
can = 3

class Hedef(pygame.sprite.Sprite):
    def __init__(self,x = width/2,y = height/2):
        super().__init__()
        self.image = pygame.Surface((target_width,target_height))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()

        self.rect.y = random.randrange(height-self.rect.height)
        self.rect.x = random.randrange(width-self.rect.width)

    def update(self, *args):
        reset = args
        global skor
        if reset:

            self.image = pygame.Surface((target_width - ((skor/10)*10) , target_height - ((skor/10)*10)))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.y = random.randrange(height - self.rect.height)
            self.rect.x = random.randrange(width - self.rect.width)

        elif reset == False:
            self.image = pygame.Surface((target_width + ((skor / 10) * 10), target_height + ((skor / 10) * 10)))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.y = random.randrange(height - self.rect.height)
            self.rect.x = random.randrange(width - self.rect.width)





hedef = Hedef()
all_sprites.add(hedef)
all_sprites.sprites()

negate = -1
create = True
aim_number = 1

####GAME###########

while True:
    clock.tick(60)
    pencere.fill((255, 255, 255))

    now_time = pygame.time.get_ticks()
    time_second = math.ceil((now_time - time) / 1000)
    if time_second > 60:
        time_minute += 1
        time = now_time


    mouseX, mouseY = pygame.mouse.get_pos()

    fontTime = font.render("{}:{}".format(time_minute,time_second),1,(150,150,150))
    fontSkor = font.render("{}".format(skor), 1, (150, 150, 150))

    pencere.blit(fontSkor, (width/2 - fontSkor.get_size()[0]/2, height/2 - fontSkor.get_size()[1]))
    pencere.blit(fontTime, (width / 2 - fontTime.get_size()[0] / 2, (height / 2 - fontTime.get_size()[1]) + fontSkor.get_size()[1]))

    all_sprites.draw(pencere)

    pencere.blit(aim, (mouseX - 30, mouseY - 30))

    if can == 3:
        pencere.blit(heart,(width-heartx,0))
        pencere.blit(heart, (width - (2*heartx), 0))
        pencere.blit(heart, (width - (3*heartx), 0))
    elif can == 2:
        pencere.blit(broke_heart, (width - broke_heartx, 0))
        pencere.blit(heart, (width - (2 * heartx), 0))
        pencere.blit(heart, (width - (3 * heartx), 0))
    elif can == 1:
        pencere.blit(broke_heart, (width - broke_heartx, 0))
        pencere.blit(broke_heart, (width - (2 * broke_heartx), 0))
        pencere.blit(heart, (width - (3 * heartx), 0))

    if skor % 10 == 0 and create == True and skor != 0:
        hedef = Hedef()
        all_sprites.add(hedef)
        aim_number += 1
        create = False
    if skor % 10 == 1:
        create = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if all_sprites.sprites()[0].rect[0]<mouseX and mouseX < all_sprites.sprites()[0].rect[0] + all_sprites.sprites()[0].image.get_size()[0] and all_sprites.sprites()[0].rect[1]<mouseY and mouseY < all_sprites.sprites()[0].rect[1] + all_sprites.sprites()[0].image.get_size()[1]:
                all_sprites.sprites()[0].update(True)
                skor += 1
            else:
                all_sprites.update(False)
                skor -= 5
                can -= 1

                for vibrate in range(0,30):
                    if negate == -1:
                        x = x + 40
                    elif negate == 1:
                        x = x - 40
                    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x, y)
                    pygame.display.set_mode((width + negate, height))
                    negate *= -1

                if skor < 0:
                    skor = 0
    #if can == 0:
        #sys.exit()


    pygame.display.update()