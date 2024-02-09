class DialogueEvent:
    # dialogue event module. actual dialogue is processed on GUI

    def __init__(self, *args):
        self.args = args
        self.object = None
        self.needs_to_be_updated = True
        self.update_on_key = True


# same thing but it ends automatically
class AutoContinuedDialogueEvent(DialogueEvent):
    def __init__(self, *args):
        super().__init__(*args)
        self.update_on_key = False
