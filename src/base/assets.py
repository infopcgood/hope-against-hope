from collections import defaultdict

import pygame.mixer

import src.constants.asset_constants as Asset_Constants


class Assets:
    """Class to store assets"""

    def __init__(self):
        self.assets = {}

    def load_asset(self, asset_path, *args):
        asset_key = asset_path + str(args) if args else asset_path
        if asset_key in self.assets.keys():
            return
        if asset_path[-4:] in Asset_Constants.SOUND_ASSET_FILENAME_EXTENSION:
            self.assets[asset_key] = pygame.mixer.Sound(asset_path)
        elif asset_path[-4:] in Asset_Constants.IMAGE_ASSET_FILENAME_EXTENSION:
            self.assets[asset_key] = pygame.image.load(asset_path).convert_alpha()
        elif asset_path[-4:] in Asset_Constants.FONT_ASSET_FILENAME_EXTENSION:
            self.assets[asset_key] = pygame.font.Font(asset_path, args[0])
        else:
            raise NotImplementedError

    def get_asset(self, asset_path, *args):
        asset_key = asset_path + str(args) if args else asset_path
        if asset_key not in self.assets.keys():
            self.load_asset(asset_path, *args)
        return self.assets[asset_key]


assets = Assets()
