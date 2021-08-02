#sprite(精靈)
import pygame

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
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))   #the image to display
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()       #定位 匡起來 #get_rect :在pygame拿一個平台
        self.rect.x = 200                       #最左上為的點 x = 200
        self.rect.y = 200
        #self.rect.center = (WIDTH / 2, HEIGHT / 2) #點設在圖片中間

    def update(self):
        self.rect.x += 2
        if self.rect.left > WIDTH:
            self.rect.right = 0

all_sprites = pygame.sprite.Group() #創建一個sprite的群組
Player = Player()                   #創一個物件
all_sprites.add(Player)             #把Player加進群組

#遊戲迴圈
running = True
while running:
    #FPS pticher at most in 1 sec
    clock.tick(FPS)
    #get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update game
    all_sprites.update()    #執行每個物件的update函式

    #display
    screen.fill((0, 0, 0))#screen.fill((R, G, B))#fill : fill in color
    all_sprites.draw(screen)    #把all_sprite內的東西全部畫出來
    pygame.display.update()

pygame.quit()

