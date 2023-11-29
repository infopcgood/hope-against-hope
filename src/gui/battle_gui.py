import pygame

import src.constants.gui_constants as GUIConstants
from src.base.assets import assets


class BattleGUI:
    def __init__(self):
        pass

    def update(self, screen: pygame.Surface, scene, main_player):
        main_player_hp_label = (assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME, GUIConstants.OPTIONS_UI_FONT_SIZE)
                                .render(f'HP: {main_player.hp:02}/{main_player.max_hp:02}', GUIConstants.TEXT_ANTI_ALIASING, (0, 0, 0)))
        screen.blit(main_player_hp_label, (10, 10))
        boss_hp_label = (assets.get_asset(GUIConstants.OPTIONS_UI_FONT_FILENAME, GUIConstants.OPTIONS_UI_FONT_SIZE)
                                .render(f'BOSS: {scene.boss.hp:02}/{scene.boss.max_hp:02}', GUIConstants.TEXT_ANTI_ALIASING, (0, 0, 0)))
        screen.blit(boss_hp_label, (876, 10))
        main_player_hp_rect = pygame.Rect(140, 10, 360 * (main_player.hp/main_player.max_hp), 22)
        screen.fill((22, 22, 188), main_player_hp_rect)
        boss_hp_rect = pygame.Rect(871 - 360 * (scene.boss.hp/scene.boss.max_hp), 10, 350 * (scene.boss.hp/scene.boss.max_hp), 22)
        screen.fill((188, 22, 22), boss_hp_rect)