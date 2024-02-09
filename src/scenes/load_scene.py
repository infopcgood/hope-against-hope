from src.scenes.scene import Scene


# scene that shows the load menu.
class LoadScene(Scene):
    def __init__(self, start_tile_x=16, start_tile_y=9):
        super().__init__(32, 18, start_tile_x, start_tile_y, "textures/map/title.png",
                         "textures/upper_layer/transparent.png", 'sounds/empty.wav', True,
                         False, False, False, [], None)
