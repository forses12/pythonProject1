import pygame
screen = pygame.display.set_mode([200, 600])
import random,model

a = pygame.image.load('images/water_drop.png')
f = pygame.image.load('images/flower1.png')
g= pygame.image.load('images/flower2.png')
def draw():
    global screen
    if model.magloire.bottom>screen.get_height():
        pygame.display.set_mode([screen.get_width()+1,screen.get_height()])
    screen.fill([0, 0, 0])
    b=pygame.transform.scale(a,[model.magloire.width,model.magloire.height])
    screen.blit(b , [model.magloire.left,model.magloire.top])

    pygame.display.flip()
