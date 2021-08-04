#sprite(精靈)
import pygame
import random

FPS = 60    #constant variable used to be all capital
WIDTH = 500
HEIGHT = 600

#初始化 ＆ 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MyFirstPygame") #change display screen's title
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)     #call initial function
        self.image = pygame.Surface((50, 40))   #the image to display
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()       #定位 匡起來 #get_rect :在pygame拿一個平台
        self.speedx = 6
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        #self.rect.x = 200                       #最左上為的點 x = 200
        #self.rect.y = 200
        #self.rect.center = (WIDTH / 2, HEIGHT - 10) #點設在圖片中間

    def update(self):
        key_pressed = pygame.key.get_pressed()  #回傳按鍵有沒有被按的布林值
        if key_pressed[pygame.K_RIGHT]:         #如果右鍵有被按 K_a a鍵
            self.rect.x += self.speedx
        elif key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self. rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)                             #add bullet into sprite group

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))   #the image to display
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()       #定位 匡起來 #get_rect :在pygame拿一個平台
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = 5
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if(self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = 2
            self.speedx = random.randrange(-2, 2)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):                   #sent player's location
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))   #the image to display
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()       #定位 匡起來 #get_rect :在pygame拿一個平台
        self.rect.centerx = x
        self.rect.buttom = y
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if(self.rect.buttom < 0):
            self.kill()

all_sprites = pygame.sprite.Group() #創建一個sprite的群組
Player = Player()                   #創一個物件
all_sprites.add(Player)             #把Player加進群組
for i in range(0, 8):
    r = Rock()
    all_sprites.add(r)

#遊戲迴圈
running = True
while running:
    #FPS pticher at most in 1 sec
    clock.tick(FPS)
    #get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    #update game
    all_sprites.update()        #執行每個物件的update函式

    #display
    screen.fill((0, 0, 0))      #screen.fill((R, G, B))#fill : fill in color
    all_sprites.draw(screen)    #把all_sprite內的東西全部畫出來
    pygame.display.update()

pygame.quit()
