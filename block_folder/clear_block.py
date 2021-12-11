from block import Block


class ClearBlock(Block):
    # This class contains the attributes and the functions for the cleared blocks_folder

    def __init__(self, x_position: int, y_position: int, image_bank: int, image_x: int, image_y: int,
                 width: int, height: int, breakable: bool):
        super().__init__(x_position, y_position, image_bank, image_x, image_y, width, height, breakable)
