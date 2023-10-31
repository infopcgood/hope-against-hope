"""scene change event module"""

class SceneChange:
    """object for event"""
    def __init__(self, desired_scene):
        self.finished = False
        self.desired_scene = desired_scene
    def run(self):
        """run scene change, does not have actual effect"""
        self.finished = True

class SceneChangeEvent:
    """Scene change event"""
    def __init__(self, desired_scene):
        self.object = SceneChange(desired_scene)
        self.needs_to_be_updated = False
        self.update_on_key = False
