"""Wait until event"""

class WaitUntil:
    """Basic waiting object class"""
    def __init__(self, condition_string, args):
        self.condition_string = condition_string
        self.args = args
        self.finished = False
    def update(self, screen):
        """waituntil object update"""
        args = self.args
        if (not self.finished) and eval(self.condition_string):
            self.finished = True

class WaitUntilEvent:
    """Basic function event class"""
    def __init__(self, condition_string, *args):
        self.object = WaitUntil(condition_string, args)
        self.needs_to_be_updated = True
        self.update_on_key = False
