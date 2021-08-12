#sprite(精靈)
import pygame
import random
import os

FPS = 60    #constant variable used to be all capital
WIDTH = 500
HEIGHT = 600

#初始化 ＆ 創建視窗
pygame.init()   #載入圖片之前要初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MyFirstPygame") #change display screen's title
clock = pygame.time.Clock()

#import image 要統一路徑寫法 使用os模組
background_img = pygame.image.load(os.path.join("img", "background.png")).convert()   #os.path : main.py所在的資料夾 
player_img = pygame.image.load(os.path.join("img", "player.png")).convert()
#rock_img = pygame.image.load(os.path.join("img", "rock.png")).convert()
bullet_img = pygame.image.load(os.path.join("img", "bullet.png")).convert()
rock_imgs = [] #一個列表
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join("img",f"rock{i}.png")).convert())   #字串前加f是可以插入變數的方法

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)     #call initial function
        self.image = pygame.transform.scale(player_img, (50, 38))    #transform.scale 可以更改圖片大小
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()       #定位 匡起來 #get_rect :在pygame拿一個平台
        self.radius = 20
        #pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
        self.speedx = 6
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        #self.rect.x = 200                      #最左上為的點 x = 200
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
        elif self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)                 #add bullet into sprite group
        bullets.add(bullet)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = random.choice(rock_imgs)  #the image to display
        self.image = self.image_ori.copy()
        self.image_ori.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()       #定位 匡起來 #get_rect :在pygame拿一個平台
        self.radius = self.rect.width * 0.85 / 2
        #pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = 5
        self.speedx = random.randrange(-3, 3)
        self.total_degree = 0
        self.rotate_degree = random.randrange(-3, 3)
    def rotate(self):
        self.total_degree += self.rotate_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center   #每一次都重新定位，才不會轉的很奇怪
        self.rect = self.image.get_rect()
        self.rect.center = center
    def update(self):
        self.rotate()
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
        self.image = bullet_img   #the image to display
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()       #定位 匡起來 #get_rect :在pygame拿一個平台
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if(self.rect.bottom < 0):
            self.kill()

#creat group
all_sprites = pygame.sprite.Group() #創建一個sprite的群組
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()                   #創一個物件
all_sprites.add(player)             #把Player加進群組
for i in range(0, 8):
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)

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
    all_sprites.update()                                            #執行每個物件的update函式
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)   #True = want to delete element 函式可以回傳字典 回傳hit 是撞到
    for hit in hits:                                                #不懂這裡用法問什麼事for
        r = Rock()
        all_sprites.add(r)
        rocks.add(r)

    hits = pygame.sprite.spritecollide(player, rocks, False, pygame.sprite.collide_circle)#player是飛船 rocks 是群組, collide會把碰撞範圍判斷換成圓形，所以要多給飛船與石頭半徑的屬性
    if hits:
        running = False
    #display
    screen.fill((0, 0, 0))              #screen.fill((R, G, B))#fill : fill in color
    screen.blit(background_img, (0, 0)) #blit : 畫到視窗的意思
    all_sprites.draw(screen)            #把all_sprite內的東西全部畫出來
    pygame.display.update()

pygame.quit()
