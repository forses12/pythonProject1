import pygame, view, time,model



while True:
    time.sleep(0.01)
    z = pygame.event.get()
    view.draw()
    model.go()

