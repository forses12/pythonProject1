import pygame, random, time


def num():
    global k
    k = [random.randint(0, 230), random.randint(0, 230), random.randint(0, 230)]


num()

magloire = pygame.Rect(random.randint(0, 550),
                       random.randint(-100, -20),
                       random.randint(3, 100),
                       random.randint(20, 100))




def go():
    global k

    if magloire.y < 401:
        magloire.y += 3
    elif magloire.y > 400:
        magloire.x =random.randint(0, 550)
        magloire.y=random.randint(-100, -20)
        magloire.w=random.randint(3, 100)
        magloire.h=random.randint(20, 100)
        num()
    if magloire.bottom >= 400:
        k = [255, 0, 0]
