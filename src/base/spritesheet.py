import pygame
import src.constants.base_constants as Constants
import src.constants.spritesheet_constants as SpriteSheet_Constants

class SpriteSheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()
    
    def image_at_rect(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        image.blit(self.spritesheet, (0, 0), rect)
        return image
    
    def image_at_anim(self, facing, anim_type, anim_index):
        return self.image_at_rect((SpriteSheet_Constants.SPRITE_WIDTH * (anim_index) , SpriteSheet_Constants.SPRITE_HEIGHT * (anim_type + facing), SpriteSheet_Constants.SPRITE_WIDTH, SpriteSheet_Constants.SPRITE_HEIGHT))