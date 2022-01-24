import pygame 
from pygame.locals import QUIT

import core

FRAME_RATE = 60

if __name__ == "__main__":
    pygame.init()
    pygame.mouse.set_visible(False)
    game = core.Game()

    clock = pygame.time.Clock()
    running = True
    while game.running and running:
        dt = clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()
        game.step(dt, pressed_keys)
        game.render()
        
    pygame.quit()
