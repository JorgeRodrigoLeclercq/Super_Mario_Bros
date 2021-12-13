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
        self.score = 0
        self.coins = 0

        # State (0 = Dead, 1 = Small, 2 = Big)
        self.state = 1

        # To stop Mario from receiving damage seconds after being hit
        self.hit_restart = 0

        # Next steps of mario
        self.next_move_right = [self.x + 16, self.y - 1]
        self.next_move_left = [self.x, self.y - 1]
        self.next_move_up = [self.x, self.y - 16]
        self.next_move_down = [self.x, self.y + 1]

    # COLLISIONS
    def collide(self, block_list: list, direction: str, start=0, end=0):
        for i in range(start, len(block_list) - end):
            for j in range(len(block_list[i])):
                if not block_list[i][j].broken:
                    if direction == "r":
                        if block_list[i][j].x_position <= self.x + 19 <= (
                                block_list[i][j].x_position + block_list[i][j].width) \
                                and block_list[i][j].y_position >= self.y + 2 >= (
                                block_list[i][j].y_position + block_list[i][j].height):
                            return True
                        else:
                            return False
                    elif direction == "l":
                        if block_list[i][j].x_position <= self.x - 3 <= (
                                block_list[i][j].x_position + block_list[i][j].width) \
                                and block_list[i][j].y_position >= self.y + 2 >= (
                                block_list[i][j].y_position + block_list[i][j].height):
                            return True
                        else:
                            return False
                    elif direction == "u":
                        if block_list[i][j].x_position <= self.x + 8 <= (
                                block_list[i][j].x_position + block_list[i][j].width) \
                                and block_list[i][j].y_position >= self.y - 3 >= (
                                block_list[i][j].y_position + block_list[i][j].height + 2):
                            return True
                        else:
                            return False
                    elif direction == "d":
                        if block_list[i][j].x_position <= self.x + 8 <= (
                                block_list[i][j].x_position + block_list[i][j].width + 2) \
                                and block_list[i][j].y_position >= self.y + 3 >= (
                                block_list[i][j].y_position + block_list[i][j].height):
                            return True
                        else:
                            return False
                else:
                    return False

    # MOVEMENT
    # Moves Mario to the right
    def move_right(self):
        # Increase the value of the x
        self.x += 1
        # States the direction of the sprite to the right
        self.sprite_direction = 16

    # Moves Mario to the left
    def move_left(self):
        # Decrease the value of the x
        self.x -= 1
        # States the direction of the sprite to the left
        self.sprite_direction = -16

    # Makes Mario jump
    def jump(self):
        # States the animation of the jump according to small mario
        if self.state == 1:
            self.animation_x = 32
            self.animation_y = 120
        # Decreases the value of y
        self.y -= 2
        # Increases the counter of the height of the jump
        self.jump_height += 2

    # Makes Mario go down after jumping
    def un_jump(self):
        # States the animation of the jump according to small mario
        if self.state == 1:
            self.animation_x = 32
            self.animation_y = 120
        # Increase the value of y
        self.y += 2

    # Updates the following moves of Mario
    def update_next_move(self):
        self.next_move_right = [self.x + 16, self.y - 1]
        self.next_move_left = [self.x - 16, self.y - 1]
        self.next_move_up = [self.x, self.y - 16]
        self.next_move_down = [self.x, self.y + 1]

    # PUNCTUATION
    # Increases the amount of coins
    def increase_coins(self):
        self.coins += 1

    # Increases the total score
    def increase_score(self, value: int):
        self.score += value

    # SPRITES
    # Changes the animation at the middle of the screen
    def middle_screen_animation(self):
        # States the direction of the sprite to de right
        self.sprite_direction = 16
        # States the animation according to small mario
        if self.state == 1:
            self.animation_x = 0
            self.animation_y = 48
        # States the animation according to big mario
        elif self.state == 2:
            self.animation_x = 0
            self.animation_y = 72

    # Changes the animation when Mario eats a mushroom
    def big_mario(self):
        # Changes the state to 2, as it is big Mario
        self.state = 2
        # States the animation according to big Mario
        self.animation_x = 0
        self.animation_y = 72

    # Change the animation when Mario gets small
    def small_mario(self):
        # Changes the state to 1, as it is small Mario
        self.state = 1
        # States the animation according to small Mario
        self.animation_x = 0
        self.animation_y = 48

    # Depending on the state choose one sprite or another
    def choose_sprite(self):
        # For small Mario
        if self.state == 1:
            self.small_mario()
        # For big Mario
        elif self.state == 2:
            self.big_mario()
