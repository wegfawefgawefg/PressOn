from enum import Enum, auto

from pygame.locals import (
    K_RIGHT,
    K_LEFT,
    K_DOWN,
    K_UP,
    K_i,
    K_t,
    K_e,
    K_p,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
)

from .scene import Scene

class Battle(Scene):
    class States(Enum):
        PLAYER_TURN = auto()

    def __init__(self, game, parent_scene):
        commands = {
        }
        super().__init__(game, commands, parent_scene)

        self.player_money = 0
        self.turn = 0
        self.state = Battle.States.PLAYER_TURN

    def render(self):
        self.game.engine.render_battle()
