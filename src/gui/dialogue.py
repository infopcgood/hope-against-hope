import pygame

import src.constants.base_constants as Constants
import src.constants.gui_constants as GUIConstants
import src.constants.sound_constants as SoundConstants
from src.base.assets import assets


# Dialogue class that makes a new instance everytime when new dialogue is displayed
class Dialogue:
    # initialize dialogue information
    def __init__(self, text, image_path=None, animation=True, sound_weight="normal", text_shaking=False):
        # set basic variables
        self.text = text
        self.text_shaking = text_shaking
        self.animation = animation
        self.typewriter_index = 0
        self.typewriter_animation_index = 0
        self.sound_weight = sound_weight
        self.finished = False
        if image_path:
            self.image = assets.get_asset(image_path)
        else:
            self.image = None

    # function that is called once when dialogue is displayed
    def show(self, screen, scene, main_player):
        pass

    # play bleep sound for each valid char
    def bleep(self, end=False):
        pygame.mixer.Channel(SoundConstants.DIALOGUE_CHANNEL).stop()
        sound_filename = ""
        if False and end:  # activates on end of string, disabled for now
            sound_filename = SoundConstants.END_DIALOGUE_SOUND_FILENAME[self.sound_weight]
        else:
            sound_filename = SoundConstants.MID_DIALOGUE_SOUND_FILENAME[self.sound_weight]
        pygame.mixer.Channel(SoundConstants.DIALOGUE_CHANNEL).play(assets.get_asset(sound_filename))

    # function that updates the dialogue(called repeatedly when dialogue is being displayed)
    def update(self, screen):
        # typewriter animation control
        label_text = self.text
        if self.animation and self.typewriter_index < len(self.text):
            if self.text[self.typewriter_index] in GUIConstants.TYPEWRITER_EXCEPT_CHARS:
                typewriter_animation_index_threshold = GUIConstants.TYPEWRITER_ANIMATION_INDEX_THRESHOLD_EXCEPT
            else:
                self.bleep()
                typewriter_animation_index_threshold = GUIConstants.TYPEWRITER_ANIMATION_INDEX_THRESHOLD_NORMAL
            self.typewriter_animation_index += 1
            if self.typewriter_animation_index >= typewriter_animation_index_threshold:
                self.typewriter_index += 1
                self.typewriter_animation_index = 0
            label_text = self.text[0:self.typewriter_index]
        elif not self.finished:
            if not self.animation:
                self.bleep(True)
            self.finished = True
        # real drawing happens here
        transparent_surface = pygame.Surface((Constants.WINDOW_WIDTH, GUIConstants.DIALOGUE_HEIGHT))
        transparent_surface.set_alpha(GUIConstants.DIALOGUE_BACKGROUND_ALPHA)
        transparent_surface.fill((0, 0, 0))
        label = assets.get_asset(GUIConstants.DIALOGUE_FONT_FILENAME, GUIConstants.DIALOGUE_GUI_FONT_SIZE).render(
            label_text,
            GUIConstants.TEXT_ANTI_ALIASING,
            GUIConstants.DIALOGUE_TEXT_COLOR)
        screen.blit(transparent_surface, (0, GUIConstants.DIALOGUE_Y))
        screen.blit(label, (
            GUIConstants.DIALOGUE_TEXT_X_WITH_IMAGE if self.image else GUIConstants.DIALOGUE_TEXT_X_NO_IMAGE,
            GUIConstants.DIALOGUE_Y + GUIConstants.DIALOGUE_TEXT_Y))
        if self.image:
            screen.blit(self.image,
                        (GUIConstants.DIALOGUE_TEXT_X_NO_IMAGE, GUIConstants.DIALOGUE_Y + GUIConstants.DIALOGUE_TEXT_Y))

    # method called when dialogue stops displaying
    def hide(self, screen, scene, main_player):
        pass
