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
        self.game_time = 400

        # Mario object
        self.mario = Mario(0, self.height - 16)

        # BLOCKS
        # Floor
        self.floor = [Floor(i, 240, 0, 32, 104, 16, 16, False, True) for i in range(0, self.floor_length, 16)]

        # Grass
        self.grass = [Grass(random.randint(0 + self.width * i, 256 + self.width * i), 224,
                            0, 16, 88, 48, 16, False, True)
                      for i in range(0, self.floor_length)]

        # Clouds
        self.clouds = [Clouds(random.randint(0 + self.width * i, 256 + self.width * i), random.randint(80, 100),
                              0, 16, 64, 48, 24, False, True)
                       for i in range(0, self.floor_length)]

        # Pipes
        self.pipes = [Pipes(288, 208, 0, 32, 0, 32, 32, False, True),
                      Pipes(528, 208, 0, 32, 0, 32, 32, False, True),
                      Pipes(848, 208, 0, 32, 0, 32, 32, False, True),
                      Pipes(200, 176, 0, 0, 120, 32, 64, False, True),
                      Pipes(1408, 208, 0, 32, 0, 32, 32, False, True)
                      ]

        # Bricks with coins
        self.coin_bricks = [CoinBrick(64, 176, 0, 0, 16, 16, 16, False, False),
                            CoinBrick(96, 176, 0, 0, 16, 16, 16, False, False),
                            CoinBrick(608, 176, 0, 0, 16, 16, 16, False, False),
                            CoinBrick(1728, 176, 0, 0, 16, 16, 16, False, False),
                            CoinBrick(304, 176, 0, 0, 16, 16, 16, False, False),
                            CoinBrick(1744, 112, 0, 0, 16, 16, 16, False, False),
                            CoinBrick(1744, 160, 0, 0, 16, 16, 16, False, False)
                            ]

        # Breakable bricks
        self.breakable_bricks = [BreakableBrick(576, 176, 0, 0, 16, 16, 16, False, False),
                                 BreakableBrick(1408, 160, 0, 0, 16, 16, 16, False, False),
                                 BreakableBrick(1728, 112, 0, 0, 16, 16, 16, False, False),
                                 BreakableBrick(320, 176, 0, 0, 16, 16, 16, False, False),
                                 BreakableBrick(288, 141, 0, 0, 16, 16, 16, False, False)
                                 ]

        # Questions blocks
        self.questions = [QuestionBlock(80, 176, 0, 16, 0, 16, 16, False, False),
                          QuestionBlock(1152, 176, 0, 16, 0, 16, 16, False, False),
                          QuestionBlock(1424, 112, 0, 16, 0, 16, 16, False, False)]

        # Flag
        self.flag = [Flag(2000, 88, 0, 224, 104, 32, 160, False, True)]

        # List with all the blocks
        self.blocks = [self.clouds, self.grass, self.pipes, self.coin_bricks,
                       self.breakable_bricks, self.questions,
                       self.floor, self.flag]

        # List with all the x and y coordinates of the blocks, including the width and height of the block
        self.blocks_x_y = []
        for i in range(2, len(self.blocks)):
            for j in range(len(self.blocks[i])):
                for k in range(self.blocks[i][j].x_position, self.blocks[i][j].x_position + self.blocks[i][j].width + 1,
                               1):
                    for w in range(self.blocks[i][j].y_position,
                                   self.blocks[i][j].y_position + self.blocks[i][j].height + 1,
                                   1):
                        self.blocks_x_y.append([k, w])

        # ENEMIES
        # Koopa Troopa
        self.koopa_troopa = [KoopaTroopa(736, 216, 0, 48, 32, 16, 24, True, False),
                             KoopaTroopa(1790, 216, 0, 48, 32, 16, 24, True, False)]

        # Goomba
        self.goomba = [Goomba(i * 256, 224, 0, 32, 48, 16, 16, True, False) for i in range(6)
                       if i != 0 or i != 3]

        # List with all the enemies
        self.enemies = [self.koopa_troopa, self.goomba]

        # SPECIAL OBJECTS
        # Mushrooms
        self.mushroom = [Mushroom(80, 157, 0, 0, 32, 16, 16, False),
                         Mushroom(1152, 157, 0, 0, 32, 16, 16, False),
                         Mushroom(1424, 93, 0, 0, 32, 16, 16, False)]
        # Coins
        self.coin = [Coin(64, 160, 0, 48, 120, 16, 16, False),
                     Coin(96, 160, 0, 48, 120, 16, 16, False),
                     Coin(608, 160, 0, 48, 120, 16, 16, False),
                     Coin(1728, 160, 0, 48, 120, 16, 16, False),
                     Coin(304, 160, 0, 48, 120, 16, 16, False),
                     Coin(1744, 96, 0, 48, 120, 16, 16, False),
                     Coin(1744, 144, 0, 48, 120, 16, 16, False)]

        # List with all the special objects
        self.special_objects = [self.mushroom, self.coin]

    ###############################################################
    ##################### UPDATE ##################################
    ###############################################################
    # Function is called each frame
    def update(self):
        # Quit the game
        if pyxel.btn(pyxel.KEY_Q) or self.mario.state == 0 or self.mario.x + 1 == self.blocks[7][0].x_position \
                or self.game_time == 0:
            pyxel.quit()

        # Decreases the value of mario.hit_restart in order for Mario to be vulnerable again
        if 150 >= self.mario.hit_restart > 0:
            self.mario.hit_restart -= 1

        # States the sprite of mario
        self.mario.choose_sprite()

        # Decreases time
        self.game_time -= .07

        # ENEMIE'S MOVEMENT
        for i in range(len(self.enemies)):
            for j in range(len(self.enemies[i])):
                # If the enemy moves to the right and there is a block, changes the direction to the left
                if self.enemies[i][j].direction:
                    if self.enemies[i][j].next_move_right in self.blocks_x_y:
                        self.enemies[i][j].direction_change()

                # If the enemy moves to the left and there is a block, changes the direction to the right
                else:
                    if self.enemies[i][j].next_move_left in self.blocks_x_y:
                        self.enemies[i][j].direction_change()
                self.enemies[i][j].update_next_move()  # Updates the following movements
                self.enemies[i][j].move()  # Moves the enemy on the correct direction

        # MARIO'S MOVEMENT
        # Updates the next position of mario
        self.mario.update_next_move()

        # Mario's movement to the right
        if pyxel.btn(pyxel.KEY_RIGHT) and self.mario.x < (
                (self.width / 2) - 16) and not self.mario.collide(self.blocks, "r", 2, 1):
            # and self.mario.next_move_right not in self.blocks_x_y
            self.mario.move_right()
            # print(self.mario.x_and_y_coordinates)

        # Mario would stop running to the right at the middle of the screen
        # Then the blocks would move to the left
        if pyxel.btn(pyxel.KEY_RIGHT) and self.mario.x == (
                (self.width / 2) - 16) and not self.mario.collide(self.blocks, "r", 2, 1):
            # and self.mario.next_move_right not in self.blocks_x_y:
            # Movement of all the blocks to the left
            for i in range(len(self.blocks)):
                for j in range(len(self.blocks[i])):
                    self.blocks[i][j].x_position -= 1
                    self.mario.middle_screen_animation()  # Changes the animation of mario

            # Movement of all the blocks to the left
            for i in range(len(self.special_objects)):
                for j in range(len(self.special_objects[i])):
                    self.special_objects[i][j].x_position -= 1

            # Updates the list of x and y coordinates of the blocks
            self.blocks_x_y = []
            for i in range(2, len(self.blocks)):
                for j in range(len(self.blocks[i])):
                    if not self.blocks[i][j].broken:
                        for k in range(self.blocks[i][j].x_position,
                                       self.blocks[i][j].x_position + self.blocks[i][j].width + 1, 1):
                            for w in range(self.blocks[i][j].y_position,
                                           self.blocks[i][j].y_position + self.blocks[i][j].height + 1, 1):
                                self.blocks_x_y.append([k, w])

        # Mario's movement to the left
        if pyxel.btn(pyxel.KEY_LEFT) and self.mario.x - 1 > 0 and not self.mario.collide(self.blocks, "l", 2, 1):
            # and self.mario.next_move_left not in self.blocks_x_y:
            self.mario.move_left()

        # Mario´s jump
        if pyxel.btn(pyxel.KEY_UP) and self.mario.jump_height <= 70 and not self.mario.collide(self.blocks, "u", 2, 1):
            # and self.mario.next_move_up not in self.blocks_x_y
            self.mario.jump()

            # Breaks the blocks that has some function
            # For through the blocks from [3 to -2] position
            for i in range(3, len(self.blocks) - 2):
                for j in range(len(self.blocks[i])):
                    # If we haven't.hit_restart yet the block and mario's coordinates are between width and height of the block
                    if not self.blocks[i][j].used and self.blocks[i][j].x_position <= self.mario.next_move_up[0] <= (
                            self.blocks[i][j].x_position + self.blocks[i][j].width) \
                            and self.blocks[i][j].y_position <= self.mario.next_move_up[1] <= (
                            self.blocks[i][j].y_position + self.blocks[i][j].height + 2):

                        # Now the block is used
                        self.blocks[i][j].used = True

                        # Finds and prints the object inside the block
                        initial_time = time.time()
                        for k in range(len(self.special_objects)):
                            for w in range(len(self.special_objects[k])):
                                if self.special_objects[k][w].x_position == self.blocks[i][j].x_position:
                                    self.special_objects[k][w].usable = True
                                    # After some time, it dissapears
                                    if time.time() - initial_time >= 3:
                                        self.special_objects[i][j].usable = False  # Now we wouldn't be able to use it
                        # Different functions of the blocks
                        # COIN BRICKS
                        if i == 3:
                            # Change the sprite, add some score and add a coin
                            self.blocks[i][j].change_to_clear_block()
                            self.mario.score += 50
                            self.mario.coins += 1
                        # BREAKABLE BRICKS
                        elif i == 4:
                            # Change the attribute of the block, now it is broken
                            self.blocks[i][j].broken = True
                        # QUESTION BLOCKS
                        elif i == 5:
                            # Change the sprite, add some score and changes the state of mario
                            self.blocks[i][j].change_to_clear_block()
                            self.mario.score += 100
                            self.mario.big_mario()

        # Gravity
        if self.mario.y <= 240 and \
                self.mario.next_move_down not in self.blocks_x_y and self.mario.jump_height > 70:
            self.mario.un_jump()

        # Regulate Mario's jumps
        if self.mario.next_move_down in self.blocks_x_y:
            self.mario.jump_height = 0

        if pyxel.btn(pyxel.KEY_UP) == False or self.mario.next_move_up in self.blocks_x_y:
            self.mario.jump_height = 71

        # MARIO VS ENEMIES
        # This loop goes through all the enemies
        for i in range(len(self.enemies)):
            for j in range(len(self.enemies[i])):
                aux = []
                # If the enemy isn't dead it appends all the positions between x to x+width and between y to y+height to a list
                if not self.enemies[i][j].dead:
                    for k in range(self.enemies[i][j].x_position,
                                   self.enemies[i][j].x_position + self.enemies[i][j].width + 1, 1):
                        for w in range(self.enemies[i][j].y_position,
                                       self.enemies[i][j].y_position + self.enemies[i][j].height + 1, 1):
                            aux.append([k, w])

                # If the next down move of mario is in the list, the enemy dies and the score increases
                if self.mario.next_move_down in aux:
                    self.enemies[i][j].dead = True
                    self.mario.increase_score(150)
                # Else if mario is.hit_restart by the right or the left, he will reduce it state once
                elif ([self.mario.x + 1, self.mario.y] in aux or [self.mario.x - 1,
                                                                  self.mario.y] in aux) and self.mario.hit_restart == 0:
                    self.mario.hit_restart = 150  # It is a variable that decrease slowly and until it isn't 0 again, any enemy can damage Mario again
                    if self.mario.state == 2:
                        self.mario.state = 1
                    elif self.mario.state == 1:
                        self.mario.state = 0
                aux.clear()
        '''self.collider = 0'''
        '''if pyxel.btn(pyxel.KEY_RIGHT):
            for i in range(len(self.blocks)):
                for j in range(len(self.blocks[i])):
                    if self.mario.x + 16 == self.blocks[i][j].x_position
                    self.collider += 1
            if self.collider == 0
                self.mario.move'''

        '''if pyxel.btn(pyxel.KEY_LEFT):
                    for i in range(len(self.blocks)):
                        for j in range(len(self.blocks[i])):
                            if self.mario.x + 16 == self.blocks[i][j].x_position + self.blocks[i][j].width'''

    ###############################################################
    ##################### DRAW ####################################
    ###############################################################
    # Draws everything in the game
    def draw(self):
        # Fill the background
        pyxel.cls(12)

        # Draw the text
        pyxel.text(4, 6, "MARIO", 7)
        pyxel.text(4, 15, "0000" + str(self.mario.score), 7)
        pyxel.blt(70, 13, 0, 48, 104, 8, 8)  # Draw the coin
        pyxel.text(80, 15, "x 0" + str(self.mario.coins), 7)
        pyxel.text(157, 6, "WORLD", 7)
        pyxel.text(157, 15, "1-1", 7)
        pyxel.text(236, 6, "TIME", 7)
        pyxel.text(236, 15, str(int(self.game_time)), 7)

        # Draws blocks
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                self.blocks[i][j].draw_block()

        # Draws enemies
        for i in range(len(self.enemies)):
            for j in range(len(self.enemies[i])):
                if not self.enemies[i][j].dead:
                    self.enemies[i][j].draw_enemy()

        # Draws special objects
        for i in range(len(self.special_objects)):
            for j in range(len(self.special_objects[i])):
                self.special_objects[i][j].draw_special_object()

        # Draws Mario
        if self.mario.state == 1 or self.mario.state == 0:
            pyxel.blt(self.mario.x, self.mario.y - 17, 0, self.mario.animation_x, self.mario.animation_y,
                      self.mario.sprite_direction, 16, colkey=12)
        if self.mario.state == 2:
            pyxel.blt(self.mario.x, self.mario.y - 32, 0, self.mario.animation_x, self.mario.animation_y,
                      self.mario.sprite_direction, 32, colkey=12)

        """ Draw Mario
        pyxel.blt(self.mario.x, self.mario.y - 17, 0, self.mario.animation_x, self.mario.animation_y,
                  self.mario.sprite_direction, 16, colkey=12)"""
