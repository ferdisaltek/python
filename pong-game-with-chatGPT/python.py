import pygame
import random


pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 60
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 5
        self.score = 0
        self.color = (255, 255, 255)

    def move(self, dy):
        if self.rect.top + dy > 0 and self.rect.bottom + dy < height:
            self.rect.move_ip(0, dy)
            self.y += dy


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.speed = [5, 5]
        self.color = (255, 255, 255)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def bounce(self):
        self.speed[0] = -self.speed[0]
        self.speed[1] = random.randint(-5, 5)


paddle1 = Paddle(30, height/2 - 30)
paddle2 = Paddle(width - 45, height/2 - 30)
ball = Ball(width/2, height/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
          #  sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle2.move(-paddle2.speed)
            elif event.key == pygame.K_DOWN:
                paddle2.move(paddle2.speed)
            elif event.key == pygame.K_w:
                paddle1.move(-paddle1.speed)
            elif event.key == pygame.K_s:
                paddle1.move(paddle1.speed)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, paddle1.color, paddle1.rect)
    pygame.draw.rect(screen, paddle2.color, paddle2.rect)
    pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)

   
