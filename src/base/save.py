import pickle
import os
import hashlib
from copy import deepcopy, copy
import base64

from src.base.assets import assets
from src.base.spritesheet import SpriteSheet


class Save:
    def __init__(self):
        pass

    def make_character_pickleable(self, character):
        spritesheet = copy(character.spritesheet)
        character.spritesheet = None
        emote_spritesheet = copy(character.emote_spritesheet)
        character.emote_spritesheet = None
        pickled_character = deepcopy(character)
        character.spritesheet = spritesheet
        character.emote_spritesheet = emote_spritesheet
        return pickled_character, character.spritesheet.filename, character.emote_spritesheet.filename

    def make_scene_pickleable(self, scene):
        background_image = copy(scene.background_image)
        scene.background_image = None
        upper_layer_image = copy(scene.upper_layer_image)
        scene.upper_layer_image = None
        pickled_scene = deepcopy(scene)
        scene.background_image = background_image
        scene.upper_layer_image = upper_layer_image
        return pickled_scene

    def get_character_from_pickle(self, pickled_character):
        character = deepcopy(pickled_character[0])
        character.spritesheet = SpriteSheet(pickled_character[1])
        character.emote_spritesheet = SpriteSheet(pickled_character[2], (32, 32))
        return character[0]

    def get_scene_from_pickle(self, pickled_scene):
        scene = deepcopy(pickled_scene)
        scene.background_image = assets.get_asset(pickled_scene.background_image_filename)
        scene.upper_layer_image = assets.get_asset(pickled_scene.upper_layer_image_filename)
        return scene

    def save_data_to_file(self, filename, scene, main_player):
        save_file = open(filename, 'wb')
        pickled_player = self.make_character_pickleable(main_player)
        pickled_scene = self.make_scene_pickleable(scene)
        save_file.write(base64.encodebytes(pickle.dumps(
            (hashlib.sha512(pickle.dumps((pickled_scene, pickled_player))).digest(), pickled_scene, pickled_player))))
        save_file.close()

    def load_data_from_file(self, filename):
        load_file = open(filename, 'rb')
        load_file_content = base64.decodebytes(load_file.read())
        data = pickle.loads(load_file_content)
        load_file.close()
        if data[0] == hashlib.sha512(pickle.dumps((data[1], data[2]))).digest():
            print(f"Save file {filename} loaded successfully.")
            return self.get_scene_from_pickle(data[1]), self.get_character_from_pickle(data[2])
        else:
            raise Exception("File is either corrupt, cracked, or damaged!")

    def delete_file(self, filename):
        os.remove(filename)
