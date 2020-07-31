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
  

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((int(screen_width),int(screen_height)))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False

  screen.fill((255, 255, 255))
  Paddle.draw(screen)
  pygame.display.update()