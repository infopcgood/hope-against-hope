import pygame

import src.constants.spritesheet_constants as SpriteSheet_Constants
import src.constants.tilemap_constants as TileMap_Constants
from src.base.spritesheet import SpriteSheet
from src.extra.functions import same_with_errors


# Base class for characters
class Character:

    def __init__(self, tile_x=16, tile_y=9, facing=SpriteSheet_Constants.FACING_RIGHT,
                 spritesheet_path='textures/spritesheets/demo.png', max_hp=20):
        # set tile x and y
        self.tile_x = tile_x
        self.tile_y = tile_y
        # set x and y and corners
        self.x = tile_x * TileMap_Constants.TILE_SIZE
        self.y = tile_y * TileMap_Constants.TILE_SIZE
        self.corner_x = self.x - 3 * 64 // 4
        self.corner_y = self.y - 64 // 2
        self.vx = 0
        self.vy = 0
        # load character spritesheet
        self.spritesheet = SpriteSheet(spritesheet_path)
        self.emote_spritesheet = SpriteSheet('textures/spritesheets/emote_balloons.png', (32, 32))
        # set default values for animation system
        self.anim = SpriteSheet_Constants.ACTION_IDLE
        self.anim_index = 0
        self.anim_preserved_index = 0
        self.anim_update_index = 0
        self.playing_anim = False
        # set status variables
        self.is_moving = False
        self.is_paralyzed = False
        self.visible = True
        # set default values for emote system
        self.emote = None
        self.emote_index = 0
        self.emote_update_index = 0
        # set character facing
        self.facing = facing
        # set rect
        self.rect = pygame.Rect(self.x - 16, self.y - 50, 32, 50)
        # set hp
        self.max_hp = max_hp
        self.hp = self.max_hp
        # 2d physics engine variables
        self.on_ground = True
        self.oncedowned = False
        # attack related variables
        self.attack_blink_cnt = -1
        self.attack_blink_idx = 0
        self.power = 5

    # force instant movement of character
    def force_instant_move(self, tile_x, tile_y):
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = tile_x * TileMap_Constants.TILE_SIZE
        self.y = tile_y * TileMap_Constants.TILE_SIZE
        self.rect = pygame.Rect(self.x - 16, self.y - 50, 32, 50)

    # force character facing
    def face(self, direction):
        self.facing = direction

    # move one tile. only called once by keypress. actually movement happens in self.move()
    def move_one_tile(self, direction, screen, scene, main_player, forced=False):
        # check if character is paralyzed
        if not forced and self.is_paralyzed:
            print("character is paralyzed!")
            return
        # set anim
        self.anim = SpriteSheet_Constants.ACTION_WALKING
        self.playing_anim = True
        # check if destination tile is valid
        if not forced:
            # out of bounds
            if (self.tile_x + TileMap_Constants.MOVEMENT_X[direction] > scene.scene_tiles_x or
                    self.tile_x + TileMap_Constants.MOVEMENT_X[direction] < 1 or
                    self.tile_y + TileMap_Constants.MOVEMENT_Y[direction] > scene.scene_tiles_y or
                    self.tile_y + TileMap_Constants.MOVEMENT_Y[direction] < 1):
                self.stop(screen, scene, main_player)
                self.facing = direction
                return
            # not movable tiles
            if not scene.movable_tiles[self.tile_y + TileMap_Constants.MOVEMENT_Y[direction]] \
                    [self.tile_x + TileMap_Constants.MOVEMENT_X[direction]]:
                self.stop(screen, scene, main_player)
                self.facing = direction
                return
            # npc is already there
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

    # animation system is controlled here
    def update_anim(self, screen, scene, main_player):
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

    # emote system, almost same as animation system
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

    # real movement happens here, depending on vx and vy
    def move(self, screen, scene, main_player, dt):
        # move character
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.rect.move_ip(self.vx * dt, self.vy * dt)

    # force stop character and correct x and y values to desired.
    def stop(self, screen, scene, main_player):
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

    # update function that is called every frame
    def update(self, screen, scene, main_player, dt, update_movements=True, is_battle=False):
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
        rect = (self.corner_x, self.corner_y, 64, 64)
        if self.visible:
            image = self.spritesheet.image_at_anim(self.facing, self.anim, self.anim_index)
            if self.attack_blink_cnt + 1:
                if self.attack_blink_cnt % 2 == 0:
                    screen.blit(image, rect)
                self.attack_blink_idx += 1
                if self.attack_blink_idx >= 8:
                    self.attack_blink_cnt += 1
                    self.attack_blink_idx = 0
                if self.attack_blink_cnt >= 7:
                    self.attack_blink_cnt = -1
            else:
                screen.blit(image, rect)
        # display emote
        if self.emote is not None:
            emote_rect = (self.x - 32, self.y - 56)
            emote_image = self.emote_spritesheet.image_at_emote(self.emote, self.emote_index)
            screen.blit(emote_image, emote_rect)

    # return if character is on ground
    def is_on_ground(self):
        return self.on_ground

    # update position by rect, used in physics engine
    def update_pos_by_rect(self):
        self.corner_x = self.rect.left
        self.corner_y = self.rect.top
        self.x = self.corner_x + 3 * 64 // 4
        self.y = self.corner_y + 64 // 2

    # start blinking when attacked
    def attacked(self, screen, scene, delta_time):
        self.attack_blink_cnt = 0
