import pygame

import src.constants.sound_constants as SoundConstants
from src.base.assets import assets


# Space class that is used for the base of Scene and Battle classes.
class Space:
    def __init__(self, width=1024, height=576, start_x=512, start_y=288, background_image="textures/map/white.png",
                 upper_layer_image="textures/upper_layer/transparent.png", bgm="", will_fade_in=True,
                 will_fade_out=True, scale_screen=True, can_save=True, events_on_load=None):
        # bgm
        self.bgm_name = bgm if bgm else None
        # fade settings
        self.will_fade_in = will_fade_in
        self.will_fade_out = will_fade_out
        self.fade_percent = 0
        self.fading = ""
        self.has_been_shown = False
        # set scene size
        self.scene_width = width
        self.scene_height = height
        # load background and upper_layer image
        self.background_image_filename = background_image
        self.background_image = assets.get_asset(background_image)
        self.upper_layer_image_filename = upper_layer_image
        self.upper_layer_image = assets.get_asset(upper_layer_image)
        # set start pos
        self.start_x = start_x
        self.start_y = start_y
        # set events on load
        self.event_on_load = events_on_load if events_on_load else []
        # define if screen should be scaled
        self.scale_screen = scale_screen
        # define if game can be saved in this space
        self.can_save = can_save

    # function that is called when space is loaded into game.
    def load(self, screen, main_player):
        # fix position
        main_player.stop(screen, self, main_player)
        # update event system
        main_player.event_active = False
        main_player.events_waiting = []
        if self.event_on_load:
            main_player.add_event_queue(screen, self, main_player, self.event_on_load)
            main_player.update_event_system(screen, self, main_player)
        # load and play bgm
        if self.bgm_name:
            if pygame.mixer.Channel(SoundConstants.BGM_CHANNEL).get_busy():
                pygame.mixer.Channel(SoundConstants.BGM_CHANNEL).stop()
            pygame.mixer.Channel(SoundConstants.BGM_CHANNEL).set_volume(SoundConstants.BGM_VOLUME)
            pygame.mixer.Channel(SoundConstants.BGM_CHANNEL).play(assets.get_asset(self.bgm_name), loops=32767)
        # run method of self which adds event to the tiles
        self.add_event_system(screen, main_player)

    # draw map on screen, called every frame
    def update_map(self, screen):
        screen.blit(self.background_image, (0, 0))

    # draw upper layer on screen, called every frame
    def update_upper_layer(self, screen):
        screen.blit(self.upper_layer_image, (0, 0))

    # assign events to tiles, can be redefined by child but is not necessary (if no tile events are needed)
    def add_event_system(self, screen, main_player):
        pass
