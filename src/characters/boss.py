from src.characters.character import Character
import src.constants.spritesheet_constants as SpriteSheet_Constants
import src.constants.tilemap_constants as TileMap_Constants


class Boss(Character):
    def __init__(self, start_x=576, start_y=288, facing=SpriteSheet_Constants.FACING_RIGHT,
                 spritesheet_path='textures/spritesheets/demo.png', max_hp=20,
                 update_strategy_function=(lambda a, b, c, d: None)):
        super().__init__(start_x // TileMap_Constants.TILE_SIZE, start_y // TileMap_Constants.TILE_SIZE, facing, spritesheet_path, max_hp)
        self.update_strategy = update_strategy_function