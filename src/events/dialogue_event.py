"""dialogue event module"""

class DialogueEvent:
    """dialogue event that effectively does nothing"""
    def __init__(self, *args):
        self.args = args
        self.object = None
        self.needs_to_be_updated = True
