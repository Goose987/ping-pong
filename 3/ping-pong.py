
from pygame import *
back = (200, 200, 200)
game = True
finish = False

speed_x = 5
speed_y = 5

win_w = 700
win_h = 500

display.set_caption('pong')
window = display.set_mode((win_w, win_h))
window.fill(back)
game = True

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed


ball = GameSprite('tenis_ball.png', 200,200, 50,50, 4)
racket_1 = Player('racket.png', 30,200, 50,150, 4)
racket_2 = Player('racket.png', 620,200, 50,150, 4)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        window.fill(back)
        if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
            speed_x *= -1


        if ball.rect.y > win_h-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200,200))

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        ball.reset()
        racket_1.reset()
        racket_1.update_l()
        racket_2.reset()
        racket_2.update_r()
    display.update()
    time.delay(10)
display.update()