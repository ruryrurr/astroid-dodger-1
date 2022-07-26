import pygame
import random
import sys
from pygame.locals import*
pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w),
                          int(screen_info.current_h))

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

num_level = 4
current_level = 1
astroid_count = 3


def main():
  while True:
    clock.tick(60)
  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()

if __name__ == "__main__":
  main()
