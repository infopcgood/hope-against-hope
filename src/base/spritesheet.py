"""Basic spritesheet module with SpriteSheet class"""
import pygame
import src.constants.spritesheet_constants as SpriteSheet_Constants
from src.base.assets import assets


class SpriteSheet:
    """Basic SpriteSheet class"""

    def __init__(self, filename, sprite_size=(64, 64)):
        # load spritesheet
        self.spritesheet = assets.get_asset(filename)
        self.sprite_size = sprite_size

    def image_at_rect(self, rectangle):
        """get image at specified rectangle"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA)
        image.blit(self.spritesheet, (0, 0), rect)
        return image

    def image_at_anim(self, facing, anim_type, anim_index):
        """get image of specified frame of animation"""
        return self.image_at_rect((self.sprite_size[0] * anim_index,
                                   self.sprite_size[1] * (
                                       anim_type if anim_type == SpriteSheet_Constants.ACTION_DEAD else anim_type + facing),
                                   self.sprite_size[0], self.sprite_size[1]))

    def image_at_emote(self, emote, emote_index):
        return self.image_at_rect(
            (self.sprite_size[0] * emote_index, self.sprite_size[1] * emote, self.sprite_size[0], self.sprite_size[1]))
