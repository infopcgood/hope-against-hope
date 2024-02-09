import pygame

import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.base.assets import assets


# class to load and manage spritesheets
class SpriteSheet:

    def __init__(self, filename, sprite_size=(64, 64)):
        # load spritesheet
        self.spritesheet = assets.get_asset(filename)
        self.filename = filename
        self.sprite_size = sprite_size

    # get image chosen by a rect
    def image_at_rect(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA)
        image.blit(self.spritesheet, (0, 0), rect)
        return image

    # get image of specified frame of animation
    def image_at_anim(self, facing, anim_type, anim_index):
        return self.image_at_rect((self.sprite_size[0] * anim_index,
                                   self.sprite_size[1] * (
                                       anim_type if anim_type == SpriteSheet_Constants.ACTION_DEAD else anim_type + facing),
                                   self.sprite_size[0], self.sprite_size[1]))

    # get image of specified frame of emote
    def image_at_emote(self, emote, emote_index):
        return self.image_at_rect(
            (self.sprite_size[0] * emote_index, self.sprite_size[1] * emote, self.sprite_size[0], self.sprite_size[1]))
