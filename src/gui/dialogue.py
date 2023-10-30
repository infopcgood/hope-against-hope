"""Basic Dialogue module containing class Dialogue"""

import pygame
import src.constants.base_constants as Constants
import src.constants.gui_constants as GUIConstants

class Dialogue:
    """Dialogue class that makes a new instance everytime when new dialogue is displayed"""
    def __init__(self, text, image_path = None, animation = True, text_shaking = False):
        """Initialize dialogue information"""
        self.text = text
        self.text_shaking = text_shaking
        self.animation = animation
        self.typewriter_index = 0
        self.typewriter_animation_index = 0
        self.animation_finished = False
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
        else:
            self.image = None
    def show(self, screen, scene, main_player):
        """function that is called once when dialogue is displayed"""
    def update(self, screen):
        """function that updates the dialogue(called repeatedly when dialogue is being displayed)"""
        # typewriter animation control
        if self.animation and self.typewriter_index < len(self.text):
            self.typewriter_animation_index += 1
            TYPEWRITER_ANIMATION_INDEX_THRESHOLD = GUIConstants.TYPEWRITER_ANIMATION_INDEX_THRESHOLD_EXCEPT if self.text[self.typewriter_index] in GUIConstants.TYPEWRITER_EXCEPT_CHARS else GUIConstants.TYPEWRITER_ANIMATION_INDEX_THRESHOLD_NORMAL
            if self.typewriter_animation_index >= TYPEWRITER_ANIMATION_INDEX_THRESHOLD:
                self.typewriter_index += 1
                self.typewriter_animation_index = 0
            label_text = self.text[0:self.typewriter_index]
        elif self.typewriter_index >= len(self.text):
            self.animation_finished = True
            label_text = self.text
        else:
            label_text = self.text
        # real drawing happenes here
        transparent_surface = pygame.Surface((Constants.WINDOW_WIDTH, GUIConstants.DIALOGUE_HEIGHT))
        transparent_surface.set_alpha(GUIConstants.DIALOGUE_BACKGROUND_ALPHA)
        transparent_surface.fill((0,0,0))
        label = GUIConstants.DIALOGUE_FONT.render(label_text, GUIConstants.TEXT_ANTI_ALIASING, GUIConstants.DIALOGUE_TEXT_COLOR)
        screen.blit(transparent_surface, (0, GUIConstants.DIALOGUE_Y))
        screen.blit(label, (GUIConstants.DIALOGUE_TEXT_X_WITH_IMAGE if self.image else GUIConstants.DIALOGUE_TEXT_X_NO_IMAGE, GUIConstants.DIALOGUE_Y + GUIConstants.DIALOGUE_TEXT_Y))
        if self.image:
            screen.blit(self.image, (GUIConstants.DIALOGUE_TEXT_X_NO_IMAGE, GUIConstants.DIALOGUE_Y + GUIConstants.DIALOGUE_TEXT_Y))
    def hide(self, screen, scene, main_player):
        """hide dialogue"""
