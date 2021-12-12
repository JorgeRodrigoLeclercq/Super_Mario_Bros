import pyxel, time

class SpecialObjects:
    # This class contains the attributes and the functions for the special objects
    def __init__(self, x_position: int, y_position: int, image_bank: int, image_x: int, image_y: int,
                 width: int, height: int, c: bool):
        # Positions
        self.x_position = x_position
        self.y_position = y_position

        # Image bank
        self.__image_bank = image_bank

        # Image coordinates
        self.image_x = image_x
        self.image_y = image_y

        # Size
        self.width = width
        self.height = height

        # Can take it or not
        self.can_use = c

    # Draws the blocks_folder
    def draw_special_object(self):
        if self.can_use:
            pyxel.blt(
                # Position of each block
                self.x_position, self.y_position,

                # Image bank
                self.__image_bank,

                # Starting point
                self.image_x, self.image_y,

                # Size of the image in the bank
                self.width, self.height,

                # To delete background color
                colkey=12
            )