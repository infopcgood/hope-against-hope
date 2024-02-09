import src.constants.base_constants as Constants


# basic delay object class
class Delay:
    def __init__(self, seconds):
        self.seconds = seconds
        self.frames = self.seconds * Constants.FPS
        self.index = 0
        self.finished = False

    # start delay
    def start(self):
        self.index = 0
        self.finished = False

    # update object and increment time
    def update(self, screen):
        if not self.finished:
            self.index += 1
            if self.index >= self.frames:
                self.finished = True


# delay in form of event
class DelayEvent:
    def __init__(self, seconds):
        self.object = Delay(seconds)
        self.needs_to_be_updated = True
        self.update_on_key = False
