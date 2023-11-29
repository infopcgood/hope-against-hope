from src.scenes.scene import Scene


class LoadScene(Scene):
    def __init__(self, start_tile_x=16, start_tile_y=9):
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/black.png",
                     "textures/upper_layer/transparent.png", '', True,
                     True, False, False, [], None)