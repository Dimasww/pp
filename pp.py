from pygame import *
window = display.set_mode((700,500))
background = transform.scale(image.load('pon.avif'),(700,500))
game = True
finish = False
FPS = 60
speed = 0.5
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self,p_image,player_speed,player_x,player_y):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(80,20))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect > 1:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x< 700-2:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 2:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect > 1:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x< 700-2:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 2:
            self.rect.y += self.speed

player1 = Player1('plat1',10,10,10)
player2 = Player2('plat',10,490,10)

while game:
        window.blit(background,(0,0))
        player1.update()
        player2.update()
        player1.reset()
        player2.reset()