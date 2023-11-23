import pygame

from src.battles.battle import Battle
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.characters.npc import NPC
from src.events.dialogue_event import DialogueEvent


class SampleBattle(Battle):
    def __init__(self, start_x=512, start_y=288):
        super().__init__(1024, 576, start_x, start_y, 'textures/map/basic_background_with_houses.png',
                         'textures/upper_layer/transparent.png',
                         'sounds/empty.wav', True, True, True, False, [], [], [],
                         None, [],
                         [pygame.Rect(0, 400, 1024, 176)], 0.0007)
