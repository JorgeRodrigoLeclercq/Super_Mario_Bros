from enemies import Enemies


class Goomba(Enemies):
    # This class is for the specific attributes and functions for Goomba

    def __init__(self, x_position: int, y: int, image_bank: int, image_x: int, image_y: int, width: int, height: int,
                 direction: bool, dead: bool):
        super().__init__(x_position, y, image_bank, image_x, image_y, width, height, direction, dead)
