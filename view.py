import pygame, random,model
screen = pygame.display.set_mode([600, 400])

a = pygame.image.load('images/water_drop.png')

def draw():
    screen.fill([0, 0, 0])
    pygame.draw.rect(screen,model.k,model.magloire)
    screen.blit(a, [100, 100])
    pygame.display.flip()
