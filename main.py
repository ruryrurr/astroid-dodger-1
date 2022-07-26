import pygame
import sys
from pygame.locals import *
from ship import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w),
                          int(screen_info.current_h))

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
screen.fill((30, 0, 30))

num_level = 4
current_level = 1
astroid_count = 3
Player = Ship((20, 200))


def main():
    for event in pygame.event.get()
    while current_level <= num_level:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.W_RIGHT:
            Player.speed[0]=10
          if event.key==pygame.S_LEFT:
            Player.speed[0]=-10
          if event.key==pygame.A_UP:
            Player.speed[0]=10
          if event.key==pygame.D_DOWN:
            Player.speed[0]=10
        screen.fill((30, 0, 30))
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
