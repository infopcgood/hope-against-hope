import base64
import datetime
import hashlib
import json
import os
import pickle
from copy import deepcopy, copy

from src.base.assets import assets
from src.base.spritesheet import SpriteSheet
from src.i18n.i18n import i18n
from src.scenes.scene import Scene


# class for managing and modifying save files. this class is only used once in this file, and other classes import the variable from this file.
class Save:
    # initialize variable, load last_saved_time
    def __init__(self):
        try:
            last_saved_time_file = open('save_datas.json', 'r')
            self.last_saved_time_json = dict(json.load(last_saved_time_file))
            last_saved_time_file.close()
        except Exception as exception:
            self.last_saved_time_json = dict(json.loads("{}"))
        self.load_needed = False
        self.load_data = None

    # remove all Surface type attributes from character to make it pickleable without modifying the original one
    def make_character_pickleable(self, character):
        spritesheet = copy(character.spritesheet)
        character.spritesheet = None
        emote_spritesheet = copy(character.emote_spritesheet)
        character.emote_spritesheet = None
        pickled_character = deepcopy(character)
        character.spritesheet = spritesheet
        character.emote_spritesheet = emote_spritesheet
        return pickled_character, character.spritesheet.filename, character.emote_spritesheet.filename

    # remove all Surface type attributes from scene to make it pickleable without modifying the original one
    def make_scene_pickleable(self, scene):
        scene.background_image = None
        scene.upper_layer_image = None
        if isinstance(scene, Scene):
            scene.npcs = [self.make_character_pickleable(npc) for npc in scene.npcs] if scene.npcs else []
        print(scene.__dict__)
        pickled_scene = deepcopy(scene)
        scene.background_image = assets.get_asset(scene.background_image_filename)
        scene.upper_layer_image = assets.get_asset(scene.upper_layer_image_filename)
        if isinstance(scene, Scene):
            scene.npcs = [self.get_character_from_pickle(npc) for npc in scene.npcs] if scene.npcs else []
        return pickled_scene

    # load pickled character and initialize deleted Surface attributes
    def get_character_from_pickle(self, pickled_character):
        character = deepcopy(pickled_character[0])
        character.spritesheet = SpriteSheet(pickled_character[1])
        character.emote_spritesheet = SpriteSheet(pickled_character[2], (32, 32))
        return character

    # load pickled scene and initialize deleted Surface attributes
    def get_scene_from_pickle(self, pickled_scene):
        scene = deepcopy(pickled_scene)
        scene.background_image = assets.get_asset(pickled_scene.background_image_filename)
        scene.upper_layer_image = assets.get_asset(pickled_scene.upper_layer_image_filename)
        if isinstance(scene, Scene):
            scene.npcs = [self.get_character_from_pickle(npc) for npc in scene.npcs] if scene.npcs else []
        return scene

    # actually save some data to file with hash
    def save_data_to_file(self, filename, scene, main_player):
        save_file = open(filename, 'wb')
        pickled_player = self.make_character_pickleable(main_player)
        pickled_scene = self.make_scene_pickleable(scene)
        # compute SHA512 hash from data and save it with the actual data, encoded in Base64 format
        # relatively easy to crack since the file is just an easily guessable pickle file, but gives some protection
        save_file.write(base64.encodebytes(pickle.dumps(
            (hashlib.sha512(pickle.dumps((pickled_scene, pickled_player))).digest(), pickled_scene, pickled_player))))
        save_file.close()
        # update last saved time
        self.last_saved_time_json[filename] = str(datetime.datetime.now())[:19]
        last_saved_time_file = open('save_datas.json', 'w')
        json.dump(self.last_saved_time_json, last_saved_time_file)
        last_saved_time_file.close()

    # load data from file with integrity check
    def load_data_from_file(self, filename):
        load_file = open(filename, 'rb')
        load_file_content = base64.decodebytes(load_file.read())
        data = pickle.loads(load_file_content)
        load_file.close()
        if data[0] == hashlib.sha512(pickle.dumps((data[1], data[2]))).digest():
            return self.get_scene_from_pickle(data[1]), self.get_character_from_pickle(data[2])
        else:
            raise Exception("File is either corrupt, cracked, or damaged!")

    # mark save as new file (overwrite last saved time data)
    def mark_as_new_file(self, filename):
        self.last_saved_time_json[filename] = i18n.get_string_from_id('new_file')
        last_saved_time_file = open('save_datas.json', 'w')
        json.dump(self.last_saved_time_json, last_saved_time_file)
        last_saved_time_file.close()

    # integrity valoidation of save file
    def validate_integrity(self, filename):
        try:
            data = self.load_data_from_file(filename)
            return True
        except Exception as e:
            print(e.message if hasattr(e, 'message') else e)
            return False

    # delete file (unused)
    def delete_file(self, filename):
        os.remove(filename)


# global variable
save = Save()
