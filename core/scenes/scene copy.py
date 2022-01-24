from pprint import pprint

class Scene:
    def __init__(self, game, commands, parent_scene=None):
        self.game = game
        self.parent_scene = parent_scene
        self.commands = commands
    
    def step(self, pressed_keys):
        if self.game.buttons_on_cooldown():
            return
        for command in self.commands:
            if pressed_keys[command]:
                self.commands[command]()
                self.game.start_button_cooldown()

    def exit(self):
        if self.parent_scene:
            self.game.scene = self.parent_scene

    def render(self):
        raise NotImplementedError