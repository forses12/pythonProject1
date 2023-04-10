import pygame

screen = pygame.display.set_mode([200,300])
import random, model

a = pygame.image.load('images/water_drop.png')
f = pygame.image.load('images/flower1.png')
g = pygame.image.load('images/flower2.png')

x_fold = f.get_height() / f.get_width()

def draw():
    global screen
    if model.magloire.bottom > screen.get_height():
        pygame.display.set_mode([screen.get_width() + 1, screen.get_height()])
    z_fold = screen.get_width() / 2
    if x_fold * z_fold<=screen.get_height():
        c = pygame.transform.scale(f, [z_fold, x_fold * z_fold])
    else:
        c=pygame.transform.scale(f, [z_fold, screen.get_height()])
    b = pygame.transform.scale(a, [model.magloire.width, model.magloire.height])

    screen.fill([0, 0, 0])

    screen.blit(c, [0, screen.get_height() - c.get_height()])
    screen.blit(b, [model.magloire.left, model.magloire.top])

    pygame.display.flip()
