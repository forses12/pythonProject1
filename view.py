import pygame

screen = pygame.display.set_mode([200,300])
import random, model

a = pygame.image.load('images/water_drop.png')
f = pygame.image.load('images/flower1.png')
g = pygame.image.load('images/flower2.png')

proportion = f.get_height() / f.get_width()

def draw():
    global screen
    flower_width=screen.get_width() / 2
    flower_height= proportion *flower_width
    if model.magloire.bottom > screen.get_height() and flower_height<screen.get_height():
        pygame.display.set_mode([screen.get_width() + 1, screen.get_height()])
    c = pygame.transform.scale(f, [flower_width, flower_height])
    v = pygame.transform.scale(g, [flower_width, flower_height])
    b = pygame.transform.scale(a, [model.magloire.width, model.magloire.height])

    screen.fill([0, 0, 0])

    screen.blit(c, [0, screen.get_height() - c.get_height()])
    screen.blit(v, [flower_width, screen.get_height() - c.get_height()])

    screen.blit(b, [model.magloire.left, model.magloire.top])

    pygame.display.flip()
