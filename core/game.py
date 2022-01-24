from os import system, name
from time import sleep

from pygame.constants import K_0
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_p,
    K_0,
    KEYDOWN,
    QUIT,
    K_RETURN,
    K_t,
    K_i,
    K_s,
)

from .scenes.main_menu import MainMenu
from .engine import Engine

class Game:
    BUTTON_COOLDOWN = 100

    def __init__(self) -> None:
        self.running = True
        self.engine = Engine(game=self) 
        self.maps = {}

        self.time = 0
        self.scene = MainMenu(self)
        self.map = None

        self.button_cooldown = 0

    def advance_clock(self):
        self.time += self.dtf

    def buttons_on_cooldown(self):
        return self.button_cooldown > 0

    def start_button_cooldown(self):
        self.button_cooldown = Game.BUTTON_COOLDOWN

    def set_current_map(self, map):
        if self.map and self.map.name == map.name:
            return
        self.map = map
        self.npcs = self.map.npcs
        self.warps = self.map.warps

    def step(self, dt, pressed_keys):
        if not self.engine:
            raise Exception("Engine not set")
        if not self.scene:
            raise Exception("No active scenes...")
        self.dt = dt
        self.dtf = dt / 1000.0
        if self.button_cooldown > 0:
            self.button_cooldown -= dt
            return
        self.scene.step(pressed_keys)
        self.advance_clock()

    def render(self):
        if not self.engine:
            return
        self.engine.clear()
        self.scene.render()
        self.engine.flip()

    def quit(self):
        self.running = False


    