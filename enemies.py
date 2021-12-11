import pyxel


class Enemies:
    # This class contains the attributes and the functions for the enemies_folder

    def __init__(self, x_position: int, y_position: int, image_bank: int, image_x: int, image_y: int,
                 width: int, height: int, direction: bool, dead: bool):
        # Positions
        self.x_position = x_position
        self.y_position = y_position

        # Image bank
        self.image_bank = image_bank

        # Image coordinates
        self.image_x = image_x
        self.image_y = image_y

        # Size
        self.width = width
        self.height = height

        # Movement direction
        self.direction = direction

        # State of the enemy
        self.dead = dead

        # Next steps of the enemy
        self.next_move_right = [self.x_position + 8, self.y_position]
        self.next_move_left = [self.x_position - 8, self.y_position]

    # Draws the enemies
    def draw_enemy(self):
        pyxel.blt(
            # Position of each block
            self.x_position, self.y_position,

            # Image bank
            self.image_bank,

            # Starting point in the image bank
            self.image_x, self.image_y,

            # Size of the image in the bank
            self.width, self.height,

            # To delete background color
            colkey=12
        )

    # Updates the following movements
    def update_next_move(self):
        self.next_move_right = [self.x_position + 16, self.y_position]
        self.next_move_left = [self.x_position - 16, self.y_position]

    # Changes the direction of the enemy's movement
    def direction_change(self):
        # True = right and False = left
        if self.direction:
            self.direction = False
        else:
            self.direction = True

    # Moves the enemy according to the direction
    def move(self):
        if self.direction:
            self.x_position += 2
        else:
            self.x_position -= 2
