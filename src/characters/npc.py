from src.characters.character import Character


# basic NPC character. only adds events on interaction
class NPC(Character):
    def __init__(self, tile_x, tile_y, facing, spritesheet_path, events_on_interaction=None):
        super().__init__(tile_x, tile_y, facing, spritesheet_path, 20)
        if events_on_interaction is None:
            events_on_interaction = []
        self.events_on_interaction = events_on_interaction
