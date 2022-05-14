
from pygame import *

window = display.set_mode((700, 500))
display.set_caption("catch up")
background = transform.scale(image.load("background.png"),(700,500))
x1 = 100
y1 = 100

x2 = 300
y2 = 300

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_h, p_w, p_speed):
        super().__init__()
        self.height = p_h
        self.width = p_w
        self.image = transform.scale(image.load(p_image), (self.width, self.height))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

sprite1right = transform.scale(image.load("sprite1right.png"),(65,65))
sprite1left = transform.scale(image.load("sprite1left.png"),(65,65))
sprite2right = transform.scale(image.load("sprite2right.png"),(65,65))
sprite2left = transform.scale(image.load("sprite2left.png"),(65,65))

sprite1 = sprite1right
sprite2 = sprite2right

speed = 10

run = True
clock = time.Clock()
FPS = 60

while run:

    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            run = False


    key_pressed = key.get_pressed()

    if key_pressed[K_LEFT] and x1 > 0:
        x1 -= speed
        sprite1 = sprite1left
    if key_pressed[K_RIGHT] and x1 < 635:
        x1 += speed
        sprite1 = sprite1right
    if key_pressed[K_UP] and y1 > 0:
        y1 -= speed
    if key_pressed[K_DOWN] and y1 < 435:
        y1 += speed

    if key_pressed[K_a] and x2 > 0:
        x2 -= speed
        sprite2 = sprite2left
    if key_pressed[K_d] and x2 < 635:
        x2 += speed
        sprite2 = sprite2right
    if key_pressed[K_w] and y2 > 0:
        y2 -= speed
    if key_pressed[K_s] and y2 < 435:
        y2 += speed

    display.update()
    clock.tick(FPS)









