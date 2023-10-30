import pygame
from src.base.spritesheet import SpriteSheet
import src.constants.base_constants as Constants
import src.constants.spritesheet_constants as SpriteSheet_Constants
import src.constants.tilemap_constants as TileMap_Constants

class Player(pygame.sprite.Sprite):
    def __init__(self, x = Constants.WINDOW_WIDTH // 2, y = Constants.WINDOW_HEIGHT // 2):
        super().__init__()
        self.x = x
        self.y = y
        self.spritesheet = SpriteSheet('textures/spritesheets/demo.png')
        self.anim = SpriteSheet_Constants.ACTION_IDLE
        self.anim_index = 0
        self.anim_update_index = 0
        self.facing = SpriteSheet_Constants.FACING_RIGHT
    
    def move(self, direction, dt):
        print("move is called!")
        self.facing = direction
        if(self.anim_update_index >= SpriteSheet_Constants.ANIM_UPDATE_THRESHOLD):
            self.anim_update_index = 0
            self.anim_index += 1
            if(self.anim_index >= SpriteSheet_Constants.ACTION_INDEX_CNT[self.anim]):
                self.anim_index = 0
        self.anim_update_index += 1
        self.x += SpriteSheet_Constants.SPEED_X[self.facing] * dt
        self.y += SpriteSheet_Constants.SPEED_Y[self.facing] * dt

    def stop(self):
        self.anim = SpriteSheet_Constants.ACTION_IDLE

    def blit(self, screen):
        rect = (self.x - SpriteSheet_Constants.SPRITE_WIDTH // 2, self.y - SpriteSheet_Constants.SPRITE_HEIGHT // 2, SpriteSheet_Constants.SPRITE_WIDTH, SpriteSheet_Constants.SPRITE_HEIGHT)
        image = self.spritesheet.image_at_anim(self.facing, self.anim, self.anim_index)
        screen.blit(image, rect)
