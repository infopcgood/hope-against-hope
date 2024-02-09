# object for Scene change
class SceneChange:

    def __init__(self, desired_scene, desired_location=None):
        self.finished = False
        if desired_location:
            self.desired_scene = desired_scene(*desired_location)
        else:
            self.desired_scene = desired_scene()

    # does not have actual effect, just marks the event finished. Actual scene change occurs in main.
    def run(self):
        self.finished = True


# scene change in form of event
class SceneChangeEvent:
    def __init__(self, desired_scene, desired_location):
        self.object = SceneChange(desired_scene, desired_location)
        self.needs_to_be_updated = False
        self.update_on_key = False
