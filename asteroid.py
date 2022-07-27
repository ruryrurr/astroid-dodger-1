import pygame
import random
class Ship(pygame.sprite.Sprite):
  def __init__(self,pos, size):
    super().__init__()
    self.image=pygame.image.load('asteroid.png')
    self.image=pygame.transform.smoothscale(self.image,size())
    self.image = pygame.transform.rotate(self.image,-90)
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = pygame.math.Vector2(0,0)
    self.speed.rotate_ip( random.randint()) 
  def update(self):
    self.rect.move_ip(self.speed)