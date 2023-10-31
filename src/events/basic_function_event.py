"""Basic function event"""

class Function:
    """basic function class"""
    def __init__(self, function):
        self.function = function
        self.finished = False
    def run(self, screen, scene, main_player):
        """run function"""
        self.function(screen, scene, main_player)
        self.finished = True
class BasicFunctionEvent:
    """Basic function event class"""
    def __init__(self, function):
        self.object = Function(function)
        self.needs_to_be_updated = False
        self.update_on_key = False
