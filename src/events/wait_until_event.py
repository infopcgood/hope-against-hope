# WARNING: EVENT IS DEPRECATED, UNUSED, AND UNSUPPORTED.

# basic waiting object class
class WaitUntil:
    def __init__(self, condition_string, args):
        self.condition_string = condition_string
        self.args = args
        self.finished = False

    # update object to recheck the conditions
    def update(self, screen):
        args = self.args
        if (not self.finished) and eval(self.condition_string):
            self.finished = True


# waiting in form of event
class WaitUntilEvent:

    def __init__(self, condition_string, *args):
        self.object = WaitUntil(condition_string, args)
        self.needs_to_be_updated = True
        self.update_on_key = False
