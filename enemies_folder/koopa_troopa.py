from enemies import Enemies


class KoopaTroopa(Enemies):
    # This class contains the specific attributes and functions for Koopa Troopa

    def __init__(self, x_position: int, y_position: int, image_bank: int, image_x: int, image_y: int, width: int,
                 height: int, direction: bool, dead: bool):
        super().__init__(x_position, y_position, image_bank, image_x, image_y, width, height, direction, dead)
