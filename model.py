import pygame, random, time


def num():
    global k
    k = [random.randint(0, 230), random.randint(0, 230), random.randint(0, 230)]

num()
screen=pygame.display.get_surface()

magloire = pygame.Rect(random.randint(10,screen.get_width()-10),
                       random.randint(-50, -20),
                       random.randint(3, 50),
                       random.randint(20, 50))





def go():
    global k

    if magloire.y <=screen.get_height():
        magloire.y += 3
    elif magloire.y > screen.get_height():
        magloire.x =random.randint(10, screen.get_width()-20)
        magloire.y=random.randint(-100, -20)
        magloire.w=random.randint(3, 50)
        magloire.h=random.randint(20,50)
        num()
    if magloire.bottom >= 400:
        k = [255, 0, 0]
