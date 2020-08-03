import pygame
import os

img_path = os.path.join('paddle.png')

class Paddle(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Paddle.image = pygame.image.load("paddle.png")
    self.image = Paddle.image
    self.image = pygame.transform.scale(self.image,(100,100))
    self.x = 200
    self.y = 200
    self.hitbox = (self.x, self.y, 205, 205)

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

  def isHit(self, width, height):
    u = False
    d = False

    if self.y == 0:
      u = True
    if self.y == height - 50:
      d = True

  def movement(self, width, height):
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN] and p.isHit(width, height).d == False:
      self.y += 1
    if key[pygame.K_UP] and p.isHit(width, height).u == False:
      self.y -= 1
  

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((int(screen_width),int(screen_height)))
p = Paddle()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False

  screen.fill((255, 255, 255))
  p.draw(screen)
  p.movement(screen_width, screen_height)
  pygame.display.update()