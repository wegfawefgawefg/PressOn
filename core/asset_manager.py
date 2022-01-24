import os
import pygame 

class AssetManager:
        def __init__(self):
            self.assets = {}
            path = os.path.dirname(os.path.abspath(__file__))
            asset_path = os.path.join(path, "assets")
            self.asset_categories = ["icons", "terrain", "units"]
            self.load_assets(asset_path)

        def load_assets(self, path):
            for category in self.asset_categories:
                self.assets[category] = self.recurse_dir(os.path.join(path, category))

        def recurse_dir(self, path):
            assets = {}
            for folder in os.listdir(path):
                assets[folder] = {}
                for file in os.listdir(os.path.join(path, folder)):
                    if file.endswith(".png"):
                        im_path = os.path.join(path, folder, file)
                        assets[folder][file[:-4]] = pygame.image.load(im_path).convert_alpha()
            return assets

        @property
        def icons(self):
            return self.assets["icons"]
        @property
        def terrain(self):
            return self.assets["terrain"]
        @property
        def units(self):
            return self.assets["units"]
