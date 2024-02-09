import pygame

from src.battles.battle import Battle


# scene only used for testing. noyb
class SampleBattle(Battle):
    def __init__(self, start_x=512, start_y=288):
        super().__init__(1024, 432, start_x, start_y, 'textures/map/basic_background_with_houses.png',
                         'textures/upper_layer/transparent.png',
                         'sounds/empty.wav', True, True, True, False, [], [], [],
                         None, [],
                         [pygame.Rect(0, 300, 1024, 132)], 0.0017)
