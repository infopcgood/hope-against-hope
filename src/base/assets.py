import json

import pygame.mixer

import src.constants.asset_constants as Asset_Constants


class Assets:
    # Asset system class

    def __init__(self):
        # assets are stored in this dictionary
        self.assets = {}

    # initially load asset onto memory
    def load_asset(self, asset_path, *args):
        asset_key = asset_path + str(args) if args else asset_path
        if asset_key in self.assets.keys():
            return
        # check asset file type
        if asset_path[-4:] in Asset_Constants.SOUND_ASSET_FILENAME_EXTENSION:
            self.assets[asset_key] = pygame.mixer.Sound(asset_path)
        elif asset_path[-4:] in Asset_Constants.IMAGE_ASSET_FILENAME_EXTENSION:
            self.assets[asset_key] = pygame.image.load(asset_path).convert_alpha()
        elif asset_path[-4:] in Asset_Constants.FONT_ASSET_FILENAME_EXTENSION:
            self.assets[asset_key] = pygame.font.Font(asset_path, args[0])
        elif asset_path[-4:] in Asset_Constants.I18N_ASSET_FILENAME_EXTENSION:
            i18n_file = open(asset_path, 'r', encoding='UTF-8')
            self.assets[asset_key] = json.load(i18n_file)
            i18n_file.close()
        else:
            raise NotImplementedError

    # get loaded asset from memory
    def get_asset(self, asset_path, *args):
        asset_key = asset_path + str(args) if args else asset_path
        if asset_key not in self.assets.keys():
            self.load_asset(asset_path, *args)
        return self.assets[asset_key]


assets = Assets()
