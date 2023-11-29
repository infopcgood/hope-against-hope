class EmoteObject:
    def __init__(self, args):
        self.args = args
        self.finished =  False
    def run(self, character):
        character.emote = self.args[0]
        self.finished = True

class PlayerEmoteEvent:
    def __init__(self, *args):
        self.needs_to_be_updated = False
        self.update_on_key = False
        self.object = EmoteObject(args)

class NPCEmoteEvent:
    def __init__(self, *args):
        self.needs_to_be_updated = False
        self.update_on_key = False
        self.object = EmoteObject(args)