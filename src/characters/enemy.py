from src.characters.character import Character
import src.constants.spritesheet_constants as SpriteSheet_Constants


class Enemy(Character):
    def __init__(self, tile_x=16, tile_y=9, facing=SpriteSheet_Constants.FACING_RIGHT,
                 spritesheet_path='textures/spritesheets/demo.png', max_hp=20,
                 update_strategy_function=(lambda a, b, c, d: None)):
        super().__init__(tile_x, tile_y, facing, spritesheet_path, max_hp)
        self.update_strategy = update_strategy_function
