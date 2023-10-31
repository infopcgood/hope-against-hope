"""Basic spritesheet module with SpriteSheet class"""
import pygame
import src.constants.spritesheet_constants as SpriteSheet_Constants

class SpriteSheet:
    """Basic SpriteSheet class"""
    def __init__(self, filename):
        # load spritesheet
        self.spritesheet = pygame.image.load(filename).convert_alpha()
    def image_at_rect(self, rectangle):
        """get image at specified rectangle"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        image.blit(self.spritesheet, (0, 0), rect)
        return image
    def image_at_anim(self, facing, anim_type, anim_index):
        """get image of specified frame of animation"""
        return self.image_at_rect((SpriteSheet_Constants.SPRITE_WIDTH * (anim_index) , SpriteSheet_Constants.SPRITE_HEIGHT * (anim_type if anim_type == SpriteSheet_Constants.ACTION_DEAD else anim_type + facing), SpriteSheet_Constants.SPRITE_WIDTH, SpriteSheet_Constants.SPRITE_HEIGHT))
