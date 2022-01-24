import time
import os
import math
from pprint import pprint
from functools import cache

import pygame 
from pygame.math import Vector2
from pygame.transform import scale

from core.asset_manager import AssetManager
from core.cam import Cam

class Engine:
    BUFFER_SIZE = (16, 9)
    TILE_SIZE = 16
    SCALE = 6

    def __init__(self, game):
        self.game = game
        self.cam = Cam(width=Engine.BUFFER_SIZE[0], height=Engine.BUFFER_SIZE[1])

        options = pygame.HWSURFACE | pygame.DOUBLEBUF #| pygame.FULLSCREEN
        screen_dims = (Engine.BUFFER_SIZE[0]*Engine.TILE_SIZE, Engine.BUFFER_SIZE[1]*Engine.TILE_SIZE)
        self.screen = pygame.Surface(screen_dims)
        self.tile_surface = pygame.Surface(((Engine.BUFFER_SIZE[0]+1)*Engine.TILE_SIZE, (Engine.BUFFER_SIZE[1]+1)*Engine.TILE_SIZE))
        self.window_screen = pygame.display.set_mode([Engine.SCALE * dim for dim in self.screen.get_size()], options)

        self.assets = AssetManager()
        pprint(self.assets.assets)
        pprint(self.assets.icons)

        pygame.font.init()
        if BUILTIN:=False:
            self.font = pygame.font.SysFont("monospace", Engine.TILE_SIZE)
        else:
            font = ["font", "pkmngb", "8bitoperator_jve"][-1]
            path = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(path, "assets","fonts",f"{font}.ttf")
            self.font = pygame.font.Font(full_path, Engine.TILE_SIZE)

        self.cam_last_position = None

    def w2p(self, pos):
        sx, sy = self.cam.to_screen_space(pos)
        return sx * self.screen.get_width(), sy * self.screen.get_height()

    def render_frame_rate(self):
        fps = self.game.dt/16*60
        color = (0, 255, 0)
        if fps < 60:    # yellow
            color = (255, 255, 0)
        elif fps < 45:  # red
            color = (255, 0, 0)
        txt = self.font.render(str(fps), Engine.SCALE, color)
        self.window_screen.blit(txt, (0, 0))

    def center_surf(self, surface, width=True, height=True):
        return (
            (self.screen.get_width() - surface.get_width())/2 if width else 0,
            (self.screen.get_height() - surface.get_height())/2 if height else 0)
    def right_align(self, surface):
        return (self.screen.get_width() - surface.get_width(), 0)

    def wigglezoom(self, surf, pos, rspeed=2, rscale=1, zspeed=2, zscale=0.1, size=1, center=(False, False)):
        surf = pygame.transform.rotozoom(surf, 
            math.sin(time.time()*rspeed)*rscale, 
            math.cos(time.time()*zspeed)*zscale+size)
        self.screen.blit(surf, (
            (pos[0] - surf.get_width()/2) if center[0] else pos[0], 
            (pos[1] - surf.get_height()/2) if center[1] else pos[1]))

    def render_battle(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_position = (
            mouse_position[0] / self.window_screen.get_width() * self.screen.get_width(),
            mouse_position[1] / self.window_screen.get_height() * self.screen.get_height())
        self.screen.blit(self.assets.icons["pointer"]["base"], mouse_position)

    def render_main_menu(self):
        txt = self.font.render("Press On", 1, (255, 255, 255))
        self.screen.blit(txt, (self.screen.get_width()/2 - txt.get_width()/2, Engine.TILE_SIZE*3))
        self.wigglezoom(self.font.render("Press Enter", 1, (255, 255, 255)),
            (self.screen.get_width()/2, Engine.TILE_SIZE*5),
            size=0.7, center=(True, True))

    def clear(self):
        self.screen.fill((0, 0, 0, 0))

    def flip(self):
        blit = pygame.transform.scale(self.screen, self.window_screen.get_size())
        self.window_screen.blit(blit, (0, 0))
        self.render_frame_rate()
        pygame.display.flip()
