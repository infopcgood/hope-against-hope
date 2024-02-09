# basic function class wrapping a function
class Function:
    def __init__(self, function):
        self.function = function
        self.finished = False

    # run function with args
    def run(self, screen, scene, main_player, args):
        self.function(screen, scene, main_player, *args)
        self.finished = True


# basic function in form of event
class BasicFunctionEvent:
    def __init__(self, function, args):
        self.object = Function(function)
        self.needs_to_be_updated = False
        self.update_on_key = False
        self.args = args
