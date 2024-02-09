# basic object for emotes
class EmoteObject:
    def __init__(self, args):
        self.args = args
        self.finished = False

    # start the emote
    def run(self, character):
        character.emote = self.args[0]
        self.finished = True


# player emote in form of event
class PlayerEmoteEvent:
    def __init__(self, *args):
        self.needs_to_be_updated = False
        self.update_on_key = False
        self.object = EmoteObject(args)


# npc emote in form of event
class NPCEmoteEvent:
    def __init__(self, *args):
        self.needs_to_be_updated = False
        self.update_on_key = False
        self.object = EmoteObject(args)
