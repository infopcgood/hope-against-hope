"""Character module with Character class that provides the base for NPCs"""

import pygame
from src.base.spritesheet import SpriteSheet
import src.constants.spritesheet_constants as SpriteSheet_Constants
import src.constants.tilemap_constants as TileMap_Constants
from src.extra.functions import same_with_errors


class Character:
    """basic character class"""

    def __init__(self, tile_x=16, tile_y=9, facing=SpriteSheet_Constants.FACING_RIGHT,
                 spritesheet_path='textures/spritesheets/demo.png', max_hp=20):
        super().__init__()
        # set tile x and y
        self.tile_x = tile_x
        self.tile_y = tile_y
        # set x and y
        self.x = tile_x * TileMap_Constants.TILE_SIZE
        self.y = tile_y * TileMap_Constants.TILE_SIZE
        self.corner_x = self.x - 3 * 64 // 4
        self.corner_y = self.y - 64 // 2
        # load character spritesheet
        self.spritesheet = SpriteSheet(spritesheet_path)
        self.emote_spritesheet = SpriteSheet('textures/spritesheets/emote_balloons.png', (32, 32))
        # set default values for animation system
        self.anim = SpriteSheet_Constants.ACTION_IDLE
        self.anim_index = 0
        self.anim_preserved_index = 0
        self.anim_update_index = 0
        self.is_moving = False
        self.is_paralyzed = False
        self.playing_anim = False
        self.visible = True
        # set default values for emote system
        self.emote = None
        self.emote_index = 0
        self.emote_update_index = 0
        # set character facing
        self.facing = facing
        self.vx = 0
        self.vy = 0
        self.rect = pygame.Rect(self.x - 16, self.y - 50, 32, 50)
        # set hp
        self.max_hp = max_hp
        self.hp = self.max_hp
        # 2d physics engine variables
        self.on_ground = True
        self.oncedowned = False

    def force_instant_move(self, tile_x, tile_y):
        """force instant movement"""
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = tile_x * TileMap_Constants.TILE_SIZE
        self.y = tile_y * TileMap_Constants.TILE_SIZE
        self.rect = pygame.Rect(self.x - 16, self.y - 50, 32, 50)

    def face(self, direction):
        """force character to face certain direction"""
        self.facing = direction

    def move_one_tile(self, direction, screen, scene, main_player, forced=False):
        """move one tile. this method is called only once and actual movement happenes in the update function"""
        if not forced and self.is_paralyzed:
            print("character is paralyzed!")
            return
        self.anim = SpriteSheet_Constants.ACTION_WALKING
        self.playing_anim = True
        # check if destination tile is valid
        if not forced:
            if (self.tile_x + TileMap_Constants.MOVEMENT_X[direction] > scene.scene_tiles_x or \
                    self.tile_x + TileMap_Constants.MOVEMENT_X[direction] < 1 or \
                    self.tile_y + TileMap_Constants.MOVEMENT_Y[direction] > scene.scene_tiles_y or \
                    self.tile_y + TileMap_Constants.MOVEMENT_Y[direction] < 1):
                self.stop(screen, scene, main_player)
                self.facing = direction
                return
            if not scene.movable_tiles[self.tile_y + TileMap_Constants.MOVEMENT_Y[direction]] \
                    [self.tile_x + TileMap_Constants.MOVEMENT_X[direction]]:
                self.stop(screen, scene, main_player)
                self.facing = direction
                return
            for npc in scene.npcs:
                if (npc.tile_x, npc.tile_y) == (main_player.tile_x + TileMap_Constants.MOVEMENT_X[direction],
                                                main_player.tile_y + TileMap_Constants.MOVEMENT_Y[direction]):
                    self.stop(screen, scene, main_player)
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
        self.vx = SpriteSheet_Constants.SPEED_X[direction]
        self.vy = SpriteSheet_Constants.SPEED_Y[direction]

    def update_anim(self, screen, scene, main_player):
        """animation is controlled here"""
        # if animation frame should be updated
        if self.anim_update_index >= SpriteSheet_Constants.ANIM_UPDATE_THRESHOLD and self.anim_index < \
                SpriteSheet_Constants.ACTION_INDEX_CNT[self.anim]:
            self.anim_update_index = 0
            self.anim_index += 1
            # if animation frame needs to be looped
            if self.anim_index >= SpriteSheet_Constants.ACTION_INDEX_CNT[self.anim]:
                if SpriteSheet_Constants.ACTION_LOOP[self.anim]:
                    self.anim_index = SpriteSheet_Constants.ACTION_START_CNT[self.anim]
                elif SpriteSheet_Constants.ACTION_STOP[self.anim]:
                    self.stop(screen, scene, main_player)
                else:
                    self.playing_anim = False
                    self.anim_index = SpriteSheet_Constants.ACTION_INDEX_CNT[self.anim] - 1
        # increment index
        self.anim_update_index += 1

    def update_emote(self, screen, scene, main_player):
        # emote animation here.
        if self.emote_update_index >= SpriteSheet_Constants.EMOTE_UPDATE_THRESHOLD and self.emote_index < \
                SpriteSheet_Constants.EMOTE_INDEX_CNT[self.emote]:
            self.emote_update_index = 0
            self.emote_index += 1
            # stop emote
            if self.emote_index >= SpriteSheet_Constants.EMOTE_INDEX_CNT[self.emote]:
                self.emote = None
                self.emote_index = 0
                self.emote_update_index = 0
        self.emote_update_index += 1

    def move(self, screen, scene, main_player, dt):
        """this is where real movement happenes."""
        # move character
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.rect.move_ip(self.vx * dt, self.vy * dt)

    def stop(self, screen, scene, main_player):
        """forcibly stop character and correct x and y values. extra arguments are for player event system"""
        # set animation variables
        self.is_moving = False
        self.playing_anim = False
        self.anim_preserved_index = self.anim_index
        self.anim_index = 0
        self.anim = SpriteSheet_Constants.ACTION_IDLE
        # correct x and y values
        self.x = self.tile_x * TileMap_Constants.TILE_SIZE
        self.y = self.tile_y * TileMap_Constants.TILE_SIZE
        self.vx = 0
        self.vy = 0

    def update(self, screen, scene, main_player, dt, update_movements=True, is_battle=False):
        """update function called every frame"""
        # move or stop character depending on position
        if update_movements and (self.is_moving or is_battle):
            self.move(screen, scene, main_player, dt)
            if same_with_errors(self.x, self.tile_x * TileMap_Constants.TILE_SIZE) and same_with_errors(
                    self.y, self.tile_y * TileMap_Constants.TILE_SIZE):
                self.stop(screen, scene, main_player)
        # continue animation
        if update_movements and self.playing_anim:
            self.update_anim(screen, scene, main_player)
        if update_movements and self.emote is not None:
            self.update_emote(screen, scene, main_player)
        self.corner_x = self.x - 3 * 64 // 4
        self.corner_y = self.y - 64 // 2
        # draw character on screen
        if self.visible:
            rect = (self.corner_x, self.corner_y, 64, 64)
            image = self.spritesheet.image_at_anim(self.facing, self.anim, self.anim_index)
            screen.blit(image, rect)
        if self.emote is not None:
            emote_rect = (self.x - 32, self.y - 56)
            emote_image = self.emote_spritesheet.image_at_emote(self.emote, self.emote_index)
            screen.blit(emote_image, emote_rect)

    def is_on_ground(self):
        return self.on_ground

    def update_pos_by_rect(self):
        self.corner_x = self.rect.left
        self.corner_y = self.rect.top
        self.x = self.corner_x + 3 * 64 // 4
        self.y = self.corner_y + 64 // 2
