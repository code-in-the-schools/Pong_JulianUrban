import pygame
import os

img_path = os.path.join("paddle.png")
img_path = os.path.join("wall.png")
img_path = os.path.join("ball.png")

class Paddle(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Paddle.image = pygame.image.load("paddle.png")
    self.image = Paddle.image
    self.image = pygame.transform.scale(self.image,(50,200))
    self.x = 50
    self.y = 200
    self.hitbox = (self.x, self.y, 55, 205)

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

  def movement(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
      self.y += 1
    if key[pygame.K_UP]:
      self.y -= 1

class Wall(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Wall.image = pygame.image.load("wall.png")
    self.image = Wall.image
    self.x = 0
    self.y = 0

  def draw(self, surface, width, height, x, y):
    surface.blit(self.image, (self.x, self.y))
    self.image = pygame.transform.scale(self.image,(width, height))
    self.x = x
    self.y = y
    self.hitbox = (x, y, width + 5, height + 5)

class Ball():
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Ball.image = pygame.image.load("ball.png")
    self.image = Ball.image
    self.image = pygame.transform.scale(self.image,(50, 50))
    self.x = 100
    self.y = 100
    self.x_velocity = 1
    self.y_velocity = 1
    self.hitbox = (self.x, self.y, 55, 55)
  
  def bounce(self):
    self.x += self.x_velocity
    self.y += self.y_velocity
    

    


pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((int(screen_width),int(screen_height)))
p = Paddle()
w = Wall()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False

  screen.fill((255, 255, 255))
  p.draw(screen)
  p.movement()
  w.draw(screen, 600, 25, 0, 0)
  w.draw(screen, 25, 600, 575, 0)
  w.draw(screen, 600, 25, 0, 575)
  pygame.display.update()