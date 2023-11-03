"""void event module"""


class Void:
    def __init__(self):
        self.finished = True


class VoidEvent:
    """void event that effectively does nothing"""

    def __init__(self, *args):
        self.args = args
        self.object = Void()
        self.needs_to_be_updated = False
        self.update_on_key = True
