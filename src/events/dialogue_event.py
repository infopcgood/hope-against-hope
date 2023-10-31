"""dialogue event module"""

class DialogueEvent:
    """dialogue event that effectively does nothing"""
    def __init__(self, *args):
        self.args = args
        self.object = None
