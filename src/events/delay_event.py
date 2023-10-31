"""Delay event"""
import src.constants.base_constants as Constants

class Delay:
    """Basic delay object class"""
    def __init__(self, seconds):
        self.seconds = seconds
        self.frames = self.seconds * Constants.FPS
        self.index = 0
        self.finished = False
    def start(self):
        """start delay"""
        self.index = 0
        self.finished = False
    def update(self, screen):
        """delay object update"""
        if not self.finished:
            self.index += 1
            if self.index >= self.frames:
                self.finished = True

class DelayEvent:
    """Basic function event class"""
    def __init__(self, seconds):
        self.object = Delay(seconds)
        self.needs_to_be_updated = True
        self.update_on_key = False
