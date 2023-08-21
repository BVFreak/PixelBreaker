import pytmx
from .lerp import lerp

class Level:
    def __init__(self):
        self.map = pytmx.load_pygame("assets/tiles/Test.tmx")
        self.tile_size = self.map.tilewidth
        self.x = 0
        self.y = 0

    def draw(self, screen):
        """_summary_

        Args:
            screen (_type_): _description_
        """
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.map.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * self.tile_size - self.x, y * self.tile_size - self.y))

    def update(self, player):
        """_summary_

        Args:
            player (_type_): _description_
        """
        target_x = player.x - 1920 / 2
        target_y = player.y - 1080 / 2

        self.x = lerp(self.x, target_x, 0.01)
        self.y = lerp(self.y, target_y, 0.01)