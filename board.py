import pyxel
import random
import time

from mario import Mario
from blocks_folder.breakable_brick import BreakableBrick
from blocks_folder.clouds import Clouds
from blocks_folder.coin_brick import CoinBrick
from blocks_folder.flag import Flag
from blocks_folder.floor import Floor
from blocks_folder.grass import Grass
from blocks_folder.pipes import Pipes
from blocks_folder.question_brick import QuestionBlock
from enemies_folder.goomba import Goomba
from enemies_folder.koopa_troopa import KoopaTroopa
from special_objects_folder.coin import Coin
from special_objects_folder.mushroom import Mushroom


class Board:
    # This class contains the attributes and the functions for the floor

    ###############################################################
    ##################### CONSTRUCTOR #############################
    ###############################################################
    def __init__(self, width: int, height: int, floor_length: int):
        # Screen size
        self.width = width
        self.height = height

        # Floor length
        self.floor_length = floor_length

        # Total time
        self.__game_time = 400

        # Mario object
        self.__mario = Mario(0, self.height - 16)

        #SCREENS
        # To begin the game
        self.__begin_game = False

        # To end the game
        self.__end_game = False

        self.__you_won_screen = False
        self.__you_failed_screen = False

        # BLOCKS
        # Floor
        self.__floor = [Floor(i, 240, 0, 32, 104, 16, 16, False, True) for i in range(0, self.floor_length, 16)]

        # Grass
        self.__grass = [Grass(random.randint(0 + self.width * i, 256 + self.width * i), 224,
                              0, 16, 88, 48, 16, False, True)
                        for i in range(0, self.floor_length)]

        # Clouds
        self.__clouds = [Clouds(random.randint(0 + self.width * i, 256 + self.width * i), random.randint(80, 100),
                                0, 16, 64, 48, 24, False, True)
                         for i in range(0, self.floor_length)]

        # Pipes
        self.__pipes = [Pipes(288, 208, 0, 32, 0, 32, 32, False, True),
                        Pipes(528, 208, 0, 32, 0, 32, 32, False, True),
                        Pipes(848, 208, 0, 32, 0, 32, 32, False, True),
                        Pipes(200, 176, 0, 0, 120, 32, 64, False, True),
                        Pipes(1408, 208, 0, 32, 0, 32, 32, False, True)
                        ]

        # Bricks with coins
        self.__coin_bricks = [CoinBrick(64, 176, 0, 0, 16, 16, 16, False, False),
                              CoinBrick(96, 176, 0, 0, 16, 16, 16, False, False),
                              CoinBrick(608, 176, 0, 0, 16, 16, 16, False, False),
                              CoinBrick(1728, 176, 0, 0, 16, 16, 16, False, False),
                              CoinBrick(352, 176, 0, 0, 16, 16, 16, False, False),
                              CoinBrick(1760, 160, 0, 0, 16, 16, 16, False, False),
                              CoinBrick(1744, 160, 0, 0, 16, 16, 16, False, False)
                              ]

        # Breakable bricks
        self.__breakable_bricks = [BreakableBrick(576, 176, 0, 0, 16, 16, 16, False, False),
                                   BreakableBrick(1408, 160, 0, 0, 16, 16, 16, False, False),
                                   BreakableBrick(1728, 112, 0, 0, 16, 16, 16, False, False),
                                   BreakableBrick(368, 176, 0, 0, 16, 16, 16, False, False),
                                   BreakableBrick(288, 141, 0, 0, 16, 16, 16, False, False)
                                   ]

        # Questions blocks
        self.__questions = [QuestionBlock(80, 176, 0, 16, 0, 16, 16, False, False),
                            QuestionBlock(1152, 176, 0, 16, 0, 16, 16, False, False),
                            QuestionBlock(1424, 112, 0, 16, 0, 16, 16, False, False)]

        # Flag
        self.__flag = [Flag(2000, 88, 0, 224, 104, 32, 160, False, True)]

        # List with all the blocks
        self.__blocks = [self.__clouds, self.__grass, self.__pipes, self.__coin_bricks,
                         self.__breakable_bricks, self.__questions,
                         self.__floor, self.__flag]

        # List with all the x and y coordinates of the blocks, including the width and height of the block
        self.__blocks_x_y = []
        for i in range(2, len(self.__blocks)):
            for j in range(len(self.__blocks[i])):
                for k in range(self.__blocks[i][j].x_position,
                               self.__blocks[i][j].x_position + self.__blocks[i][j].width + 1,
                               1):
                    for w in range(self.__blocks[i][j].y_position,
                                   self.__blocks[i][j].y_position + self.__blocks[i][j].height + 1,
                                   1):
                        self.__blocks_x_y.append([k, w])

        # ENEMIES
        # Koopa Troopa
        self.__koopa_troopa = [KoopaTroopa(736, 216, 0, 48, 32, 16, 24, True, False),
                               KoopaTroopa(1850, 216, 0, 48, 32, 16, 24, True, False)]

        # Goomba
        self.__goomba = [Goomba(i * 256, 224, 0, 32, 48, 16, 16, True, False) for i in range(6) if i != 0 and i != 3]

        # List with all the enemies
        self.__enemies = [self.__koopa_troopa, self.__goomba]

        # SPECIAL OBJECTS
        # Mushrooms
        self.__mushroom = [Mushroom(80, 157, 0, 0, 32, 16, 16, False),
                           Mushroom(1152, 157, 0, 0, 32, 16, 16, False),
                           Mushroom(1424, 93, 0, 0, 32, 16, 16, False)]
        # Coins
        self.__coin = [Coin(64, 160, 0, 48, 120, 16, 16, False),
                       Coin(96, 160, 0, 48, 120, 16, 16, False),
                       Coin(608, 160, 0, 48, 120, 16, 16, False),
                       Coin(1728, 160, 0, 48, 120, 16, 16, False),
                       Coin(352, 160, 0, 48, 120, 16, 16, False),
                       Coin(1760, 144, 0, 48, 120, 16, 16, False),
                       Coin(1744, 144, 0, 48, 120, 16, 16, False)]

        # List with all the special objects
        self.__special_objects = [self.__mushroom, self.__coin]

    ###############################################################
    ##################### UPDATE ##################################
    ###############################################################
    # Function is called each frame
    def update(self):

        if pyxel.btn(pyxel.KEY_ENTER) or self.__begin_game:
            self.__begin_game = True

            # Quit the game
            if pyxel.btn(pyxel.KEY_Q):
                pyxel.quit()

            # States the sprite of mario
            self.__mario.choose_sprite()

            # Decreases time
            self.__game_time -= .07

            # ENEMIE'S MOVEMENT
            for i in range(len(self.__enemies)):
                for j in range(len(self.__enemies[i])):
                    # If the enemy moves to the right and there is a block, changes the direction to the left
                    if self.__enemies[i][j].direction:
                        if self.__enemies[i][j].next_move_right in self.__blocks_x_y:
                            self.__enemies[i][j].direction_change()

                    # If the enemy moves to the left and there is a block, changes the direction to the right
                    else:
                        if self.__enemies[i][j].next_move_left in self.__blocks_x_y:
                            self.__enemies[i][j].direction_change()
                    self.__enemies[i][j].update_next_move()  # Updates the following movements
                    self.__enemies[i][j].move()  # Moves the enemy on the correct direction

            # MARIO'S MOVEMENT

            # Updates the next position of mario
            self.__mario.update_next_move()

            # Mario's movement to the right
            if pyxel.btn(pyxel.KEY_RIGHT) and self.__mario.x < ((self.width / 2) - 16) \
                    and self.__mario.next_move_right not in self.__blocks_x_y:
                self.__mario.move_right()

            # Mario would stop running to the right at the middle of the screen
            # Then the blocks would move to the left
            if pyxel.btn(pyxel.KEY_RIGHT) and self.__mario.x == ((self.width / 2) - 16) \
                    and self.__mario.next_move_right not in self.__blocks_x_y:
                # Movement of all the blocks to the left
                for i in range(len(self.__blocks)):
                    for j in range(len(self.__blocks[i])):
                        self.__blocks[i][j].x_position -= 1
                        self.__mario.middle_screen_animation()  # Changes the animation of mario

                for i in range(len(self.__blocks_x_y)):
                    self.__blocks_x_y[i][0] -= 1

                # Movement of all the blocks to the left
                for i in range(len(self.__special_objects)):
                    for j in range(len(self.__special_objects[i])):
                        self.__special_objects[i][j].x_position -= 1

            # Mario's movement to the left
            if pyxel.btn(pyxel.KEY_LEFT) and self.__mario.x - 1 > 0 \
                    and self.__mario.next_move_left not in self.__blocks_x_y:
                self.__mario.move_left()

            # Mario´s jump
            if pyxel.btn(pyxel.KEY_UP) and self.__mario.jump_height <= 70 \
                    and self.__mario.next_move_up not in self.__blocks_x_y:
                # and self.__mario.next_move_up not in self.__blocks_x_y
                self.__mario.jump()

                # Breaks the blocks that has some function
                # For through the blocks from [3 to -2] position
                for i in range(3, len(self.__blocks) - 2):
                    for j in range(len(self.__blocks[i])):
                        # If we haven't.hit_restart yet the block and mario's coordinates are between width and height of
                        # the block
                        if not self.__blocks[i][j].used and self.__blocks[i][j].x_position <= self.__mario.next_move_up[
                            0] <= (
                                self.__blocks[i][j].x_position + self.__blocks[i][j].width) \
                                and self.__blocks[i][j].y_position <= self.__mario.next_move_up[1] <= (
                                self.__blocks[i][j].y_position + self.__blocks[i][j].height + 2):

                            # Now the block is used
                            self.__blocks[i][j].used = True

                            # Finds and prints the object inside the block
                            for k in range(len(self.__special_objects)):
                                for w in range(len(self.__special_objects[k])):
                                    if self.__special_objects[k][w].x_position == self.__blocks[i][j].x_position:
                                        self.__special_objects[k][w].usable = True

                            # Different functions of the blocks
                            # COIN BRICKS
                            if i == 3:
                                # Change the sprite, add some score and add a coin
                                self.__blocks[i][j].change_to_clear_block()
                                self.__mario.score += 50
                                self.__mario.coins += 1
                            # BREAKABLE BRICKS
                            elif i == 4:
                                if self.__mario.state == 2:
                                    # Change the attribute of the block, now it is broken
                                    self.__blocks[i][j].broken = True
                            # QUESTION BLOCKS
                            elif i == 5:
                                # Change the sprite, add some score and changes the state of mario
                                self.__blocks[i][j].change_to_clear_block()
                                self.__mario.score += 100
                                self.__mario.big_mario()

            # Gravity
            if self.__mario.y <= 240 and \
                    self.__mario.next_move_down not in self.__blocks_x_y and self.__mario.jump_height > 70:
                self.__mario.un_jump()

            # Regulate Mario's jumps
            if self.__mario.next_move_down in self.__blocks_x_y:
                self.__mario.jump_height = 0

            if pyxel.btn(pyxel.KEY_UP) == False or self.__mario.next_move_up in self.__blocks_x_y:
                self.__mario.jump_height = 71

            # MARIO VS ENEMIES
            # This loop goes through all the enemies
            for i in range(len(self.__enemies)):
                for j in range(len(self.__enemies[i])):
                    aux = []
                    # If the enemy isn't dead it appends all the positions between x to x+width and between y to
                    # y+height
                    if not self.__enemies[i][j].dead:
                        for k in range(self.__enemies[i][j].x_position,
                                       self.__enemies[i][j].x_position + self.__enemies[i][j].width + 1, 1):
                            for w in range(self.__enemies[i][j].y_position,
                                           self.__enemies[i][j].y_position + self.__enemies[i][j].height + 1, 1):
                                aux.append([k, w])

                    # If the next down move of mario is in the list, the enemy dies and the score increases
                    if [self.__mario.next_move_down[0], self.__mario.next_move_down[1] + 1] in aux:
                        self.__enemies[i][j].dead = True
                        self.__mario.increase_score(150)
                    # Else if mario is.hit_restart by the right or the left, he will reduce it state once
                    elif ([self.__mario.x + 1, self.__mario.y] in aux or [self.__mario.x - 1,
                                                                          self.__mario.y] in aux) and self.__mario.hit_restart == 0:
                        self.__mario.hit_restart = 150  # Makes Mario vulnerable for 150 frames
                        if self.__mario.state == 2:
                            self.__mario.state = 1
                        elif self.__mario.state == 1:
                            self.__mario.state = 0
                    aux.clear()

            # Decreases the value of mario.hit_restart in order for Mario to be vulnerable again
            if 150 >= self.__mario.hit_restart > 0:
                self.__mario.hit_restart -= 1

        # To end the game if you fail
        if self.__mario.state == 0 or self.__game_time <= 0:
            self.__you_failed_screen = True
            self.__begin_game = False

        # To end the game if you win
        if self.__mario.x + 32 >= self.__blocks[7][0].x_position:
            self.__you_won_screen = True
            self.__begin_game = False

    ###############################################################
    ########################## DRAW ###############################
    ###############################################################
    # Draws everything in the game
    def draw(self):

        # Initial screen
        if not self.__begin_game and not self.__you_won_screen and not self.__you_failed_screen:
            pyxel.cls(0)
            pyxel.text(75, self.height // 2, "WELCOME TO SUPER MARIO BROS\n PRESS ENTER TO CONTINUE", 7)

        # Game
        elif self.__begin_game:
            # Fill the background
            pyxel.cls(12)

            # Draw the text
            pyxel.text(4, 6, "MARIO", 7)
            pyxel.text(4, 15, "0000" + str(self.__mario.score), 7)
            pyxel.blt(70, 13, 0, 48, 104, 8, 8)  # Draw the coin
            pyxel.text(80, 15, "x 0" + str(self.__mario.coins), 7)
            pyxel.text(157, 6, "WORLD", 7)
            pyxel.text(157, 15, "1-1", 7)
            pyxel.text(236, 6, "TIME", 7)
            pyxel.text(236, 15, str(int(self.__game_time)), 7)

            # Draws blocks
            for i in range(len(self.__blocks)):
                for j in range(len(self.__blocks[i])):
                    self.__blocks[i][j].draw_block()

            # Draws enemies
            for i in range(len(self.__enemies)):
                for j in range(len(self.__enemies[i])):
                    if not self.__enemies[i][j].dead:
                        self.__enemies[i][j].draw_enemy()

            # Draws special objects
            for i in range(len(self.__special_objects)):
                for j in range(len(self.__special_objects[i])):
                    self.__special_objects[i][j].draw_special_object()

            # Draws Mario
            if self.__mario.state == 1:
                pyxel.blt(self.__mario.x, self.__mario.y - 17, 0, self.__mario.animation_x, self.__mario.animation_y,
                          self.__mario.sprite_direction, 16, colkey=12)
            elif self.__mario.state == 2:
                pyxel.blt(self.__mario.x, self.__mario.y - 32, 0, self.__mario.animation_x, self.__mario.animation_y,
                          self.__mario.sprite_direction, 32, colkey=12)

        # Fail screen
        elif self.__you_failed_screen:
            pyxel.cls(0)
            pyxel.text(100, self.height // 2, "YOU FAILED", 7)

        # Win screen
        elif self.__you_won_screen:
            pyxel.cls(0)
            pyxel.text(115, self.height // 2, "YOU WON", pyxel.frame_count%16)

