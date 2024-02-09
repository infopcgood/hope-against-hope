# V O I D
class Void:
    def __init__(self):
        self.finished = True


# empty event object that waits for a single keypress
class VoidEvent:
    def __init__(self, *args):
        self.args = args
        self.object = Void()
        self.needs_to_be_updated = False
        self.update_on_key = True
