import pygame
import sys
from pygame.locals import*
from ship import*

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w),
                          int(screen_info.current_h))

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
screen.fill((30, 0, 0))

num_level = 4
current_level = 1
astroid_count = 3
Player = Ship((20, 200))
Astroids = pygame.sprite.Clock()

def init():
  global astroid_count, Astroids
  Player.reset((20, 200))
  Astroids.empty()
  astroid_count+=3
  Astroids.add(Asteroid((random.randint(50, width - 50), random.randint(50, height - 50)), random.randint(15, 60))
)
  

def main():
  global current_level, num_level  
  while current_level <= num_level:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
          Player.speed[0]=10
        if event.key==pygame.K_LEFT:
          Player.speed[0]=-10
        if event.key==pygame.K_UP:
          Player.speed[1]=-10
        if event.key==pygame.K_DOWN:
          Player.speed[1]=10
              #releasing the key
      if event.type==pygame.KEYUP:
        if event.key==pygame.K_RIGHT:
          Player.speed[0]=0
        if event.key==pygame.K_LEFT:
          Player.speed[0]=0
        if event.key==pygame.K_UP:
          Player.speed[1]=0
        if event.key==pygame.K_DOWN:
          Player.speed[1]=0
        if pygame.sprite.spritecollide(Player, Astroid)

            
    Player.update()
    screen.fill((30,0,30))
    screen.blit(Player.image, Player.rect)
    pygame.display.flip()
    Astroids.update()
    Astroids.draw(screen)
    get_hit = pygame.sprit.collide(Players,Astroids, False)
    if player.checkReset(width):
      init()
    elif get_hit
      Player.checkReset(20,200)
      

if __name__ == "__main__":
    main()


    
  