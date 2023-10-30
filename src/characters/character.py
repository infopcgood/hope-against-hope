"""Character module with Character class that provides the base for NPCs"""

import pygame
from src.base.spritesheet import SpriteSheet
import src.constants.spritesheet_constants as SpriteSheet_Constants
import src.constants.tilemap_constants as TileMap_Constants

class Character(pygame.sprite.Sprite):
    """basic character class"""
    def _sameWithErrors(self, a, b, error = 1):
        """hidden method for error correction"""
        return bool(abs(a-b)<=error)
    def __init__(self, tile_x = TileMap_Constants.TILEMAP_WIDTH // 2, tile_y = TileMap_Constants.TILEMAP_HEIGHT // 2, facing = SpriteSheet_Constants.FACING_RIGHT, spritesheet_path = 'textures/spritesheets/demo.png'):
        super().__init__()
        # set tile x and y
        self.tile_x = tile_x
        self.tile_y = tile_y
        # set x and y
        self.x = tile_x * TileMap_Constants.TILE_SIZE
        self.y = tile_y * TileMap_Constants.TILE_SIZE
        # load character spritesheet
        self.spritesheet = SpriteSheet(spritesheet_path)
        # set default values for animation system
        self.anim = SpriteSheet_Constants.ACTION_IDLE
        self.anim_index = 0
        self.anim_preserved_index = 0
        self.anim_update_index = 0
        self.is_moving = False
        # set character facing
        self.facing = facing
    def force_instant_move(self, tile_x, tile_y):
        """force instant movement"""
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = tile_x * TileMap_Constants.TILE_SIZE
        self.y = tile_y * TileMap_Constants.TILE_SIZE
    def face(self, direction):
        """force character to face certain direction"""
        self.facing = direction
    def move_one_tile(self, direction, scene):
        """move one tile. this method is called only once and actual movement happenes in the update function"""
        # check if destination tile is valid
        if self.tile_x + TileMap_Constants.MOVEMENT_X[direction] > TileMap_Constants.TILEMAP_X_MAX or self.tile_x + TileMap_Constants.MOVEMENT_X[direction] < TileMap_Constants.TILEMAP_X_MIN:
            return
        if self.tile_y + TileMap_Constants.MOVEMENT_Y[direction] > TileMap_Constants.TILEMAP_Y_MAX or self.tile_y + TileMap_Constants.MOVEMENT_Y[direction] < TileMap_Constants.TILEMAP_Y_MIN:
            return
        if not scene.movable_tiles[self.tile_y + TileMap_Constants.MOVEMENT_Y[direction]][self.tile_x + TileMap_Constants.MOVEMENT_X[direction]]:
            self.facing = direction
            return
        # check if animation could be resumed (constant keypress detected)
        if self.facing == direction:
            self.anim_index = self.anim_preserved_index
        self.facing = direction
        # set movement variables
        self.is_moving = True
        self.tile_x += TileMap_Constants.MOVEMENT_X[direction]
        self.tile_y += TileMap_Constants.MOVEMENT_Y[direction]
    def move(self, dt):
        """this is where real movement happenes."""
        # if animation frame should be updated
        if self.anim_update_index >= SpriteSheet_Constants.ANIM_UPDATE_THRESHOLD:
            self.anim_update_index = 0
            self.anim_index += 1
            # if animation frame needs to be looped
            if self.anim_index >= SpriteSheet_Constants.ACTION_INDEX_CNT[self.anim]:
                self.anim_index = SpriteSheet_Constants.ACTION_START_CNT[self.anim]
        # increment index
        self.anim_update_index += 1
        # move character
        self.x += SpriteSheet_Constants.SPEED_X[self.facing] * dt
        self.y += SpriteSheet_Constants.SPEED_Y[self.facing] * dt
    def stop(self, screen, scene, main_player):
        """forcibly stop character and correct x and y values. extra arguments are for player event system"""
        # set animation variables
        self.is_moving = False
        self.anim_preserved_index = self.anim_index
        self.anim_index = 0
        self.anim = SpriteSheet_Constants.ACTION_IDLE
        # correct x and y values
        self.x = self.tile_x * TileMap_Constants.TILE_SIZE
        self.y = self.tile_y * TileMap_Constants.TILE_SIZE
    def update(self, screen, scene, main_player, dt):
        """update function called every frame"""
        # move or stop character depending on position
        if self.is_moving:
            self.move(dt)
        if self.is_moving and self._sameWithErrors(self.x, self.tile_x * TileMap_Constants.TILE_SIZE) and self._sameWithErrors(self.y, self.tile_y * TileMap_Constants.TILE_SIZE):
            self.stop(screen, scene, main_player)
        # draw character on screen
        rect = (self.x - 3 * SpriteSheet_Constants.SPRITE_WIDTH // 4, self.y - SpriteSheet_Constants.SPRITE_HEIGHT // 2, SpriteSheet_Constants.SPRITE_WIDTH, SpriteSheet_Constants.SPRITE_HEIGHT)
        image = self.spritesheet.image_at_anim(self.facing, self.anim, self.anim_index)
        screen.blit(image, rect)
