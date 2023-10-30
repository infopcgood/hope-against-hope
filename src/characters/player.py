import pygame
from src.base.spritesheet import SpriteSheet
import src.constants.base_constants as Constants
import src.constants.spritesheet_constants as SpriteSheet_Constants
import src.constants.tilemap_constants as TileMap_Constants

def sameWithErrors(a, b, error = 1):
    return bool(abs(a-b)<=error)

class Player(pygame.sprite.Sprite):
    def __init__(self, x = Constants.WINDOW_WIDTH // 2, y = Constants.WINDOW_HEIGHT // 2):
        super().__init__()
        self.x = x
        self.y = y
        self.tile_x = x // TileMap_Constants.TILE_SIZE
        self.tile_y = y // TileMap_Constants.TILE_SIZE
        self.spritesheet = SpriteSheet('textures/spritesheets/demo.png')
        self.anim = SpriteSheet_Constants.ACTION_IDLE
        self.anim_index = 0
        self.anim_preserved_index = 0
        self.anim_update_index = 0
        self.is_moving = False
        self.facing = SpriteSheet_Constants.FACING_RIGHT
    
    def force_instant_move(self, tile_x, tile_y):
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = tile_x * TileMap_Constants.TILE_SIZE
        self.y = tile_y * TileMap_Constants.TILE_SIZE
    
    def move_one_tile(self, direction, movable_tiles):
        # check if destination tile is valid
        if self.tile_x + TileMap_Constants.MOVEMENT_X[direction] > TileMap_Constants.TILEMAP_X_MAX or self.tile_x + TileMap_Constants.MOVEMENT_X[direction] < TileMap_Constants.TILEMAP_X_MIN:
            return
        if self.tile_y + TileMap_Constants.MOVEMENT_Y[direction] > TileMap_Constants.TILEMAP_Y_MAX or self.tile_y + TileMap_Constants.MOVEMENT_Y[direction] < TileMap_Constants.TILEMAP_Y_MIN:
            return
        if not movable_tiles[self.tile_y + TileMap_Constants.MOVEMENT_Y[direction]][self.tile_x + TileMap_Constants.MOVEMENT_X[direction]]:
            self.facing = direction
            return
        if self.facing == direction:
            self.anim_index = self.anim_preserved_index
        self.facing = direction
        self.is_moving = True
        self.tile_x += TileMap_Constants.MOVEMENT_X[direction]
        self.tile_y += TileMap_Constants.MOVEMENT_Y[direction]

    def move(self, direction, dt):
        if(self.anim_update_index >= SpriteSheet_Constants.ANIM_UPDATE_THRESHOLD):
            self.anim_update_index = 0
            self.anim_index += 1
            if(self.anim_index >= SpriteSheet_Constants.ACTION_INDEX_CNT[self.anim]):
                self.anim_index = SpriteSheet_Constants.ACTION_START_CNT[self.anim]
        self.anim_update_index += 1
        self.x += SpriteSheet_Constants.SPEED_X[self.facing] * dt
        self.y += SpriteSheet_Constants.SPEED_Y[self.facing] * dt

    def stop(self):
        self.is_moving = False
        self.anim_preserved_index = self.anim_index
        self.anim_index = 0
        self.anim = SpriteSheet_Constants.ACTION_IDLE

    def update(self, screen, dt):
        if self.is_moving:
            self.move(self.facing, dt)
        if sameWithErrors(self.x, self.tile_x * TileMap_Constants.TILE_SIZE) and sameWithErrors(self.y, self.tile_y * TileMap_Constants.TILE_SIZE):
            self.stop()
            self.x = self.tile_x * TileMap_Constants.TILE_SIZE
            self.y = self.tile_y * TileMap_Constants.TILE_SIZE
        rect = (self.x - 3 * SpriteSheet_Constants.SPRITE_WIDTH // 4, self.y - SpriteSheet_Constants.SPRITE_HEIGHT // 2, SpriteSheet_Constants.SPRITE_WIDTH, SpriteSheet_Constants.SPRITE_HEIGHT)
        image = self.spritesheet.image_at_anim(self.facing, self.anim, self.anim_index)
        screen.blit(image, rect)
