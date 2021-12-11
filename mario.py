import pyxel


class Mario:
    # This class contains all the attributes and functions for Mario

    def __init__(self, x, y):
        # Mario position
        self.x = x
        self.y = y

        # Mario animation
        self.sprite_direction = 16
        self.animation_x = 0
        self.animation_y = 48

        # Height of Mario's jump
        self.jump_height = 0

        # Punctuation
        self.score = 20
        self.coins = 0

        # State (0 = Dead, 1 = Small, 2 = Big)
        self.state = 2

        # Mario has been hit by an enemy
        self.hit = 0

        # Next steps of mario
        self.next_move_right = [self.x + 16, self.y - 1]
        self.next_move_left = [self.x - 16, self.y - 1]
        self.next_move_up = [self.x, self.y - 16]
        self.next_move_down = [self.x, self.y + 2]

        # List of Mario's sprite x and y coordinates
        '''self.x_and_y_coordinates = []
        for i in range(self.x, self.x + 16):
            for j in range(self.y, self.y + 16):
                self.x_and_y_coordinates.append([i, j])'''

    # Moves Mario to the right
    def move_right(self):
        self.x += 1
        self.sprite_direction = 16

    # Moves Mario to the left
    def move_left(self):
        self.x -= 1
        self.sprite_direction = -16

    # Makes Mario jumps
    def jump(self):
        if self.state==1:
            self.animation_x = 32
            self.animation_y = 120
        self.y -= 2
        self.jump_height += 2

    # Makes Mario go down after jumping
    def un_jump(self):
        if self.state == 1:
            self.animation_x = 32
            self.animation_y = 120
        self.y += 2

    # Updates the following moves of Mario
    def update_next_move(self):
        self.next_move_right = [self.x + 16, self.y - 1]
        self.next_move_left = [self.x - 16, self.y - 1]
        self.next_move_up = [self.x, self.y - 16]
        self.next_move_down = [self.x, self.y + 1]

    # Increases the amount of coins
    def increase_coins(self):
        self.coins += 1

    # Increases the total score
    def increase_score(self, value: int):
        self.score += value

    # SPRITES OF MARIO

    # Change the animation at the middle of the screen
    def middle_screen_animation(self):
        self.sprite_direction = 16
        self.animation_x = 0
        self.animation_y = 48

    # Change the animation when mario eats a mushroom
    def big_mario(self):
        self.animation_x = 0
        self.animation_y = 72

    # Change the animation when mario gets small
    def small_mario(self):
        self.animation_x = 0
        self.animation_y = 48

    # Depending on the state choose one sprite or another
    def choose_sprite(self):
        if self.state == 1:
            self.small_mario()
        elif self.state == 2:
            self.big_mario()