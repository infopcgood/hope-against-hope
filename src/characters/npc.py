import pygame.sprite

from src.characters.character import Character


class NPC(Character):
    def __init__(self, tile_x, tile_y, facing, spritesheet_path, events_on_interaction=[]):
        super().__init__(tile_x, tile_y, facing, spritesheet_path)
        self.events_on_interaction = events_on_interaction
