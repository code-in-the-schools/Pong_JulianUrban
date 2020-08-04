import pygame
import os

img_path = os.path.join('paddle.png')
img_path = os.path.join("wall.png")

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
  w.draw(screen, 600, 50, 0, 0)
  w.draw(screen, 50, 600, 550, 0)
  w.draw(screen, 600, 50, 0, 550)
  pygame.display.update()