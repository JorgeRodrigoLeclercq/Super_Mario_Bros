import pyxel
import random

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
from mario import Mario
from special_objects_folder.coin import Coin
from special_objects_folder.mushroom import Mushroom


class Board:
    # This class contains the attributes and the functions for the floor

    def __init__(self, w: int, h: int, f: int):
        # Screen size
        self.width = w
        self.height = h

        # Floor length
        self.floor_length = f

        # Total time
        self.game_time = 400

        # Mario object
        self.mario = Mario(0, self.height - 16)

#######################################################################################################################
        # BLOCKS
        # Floor
        self.floor = [Floor(i, 240, 0, 32, 104, 16, 16, False) for i in range(0, self.floor_length, 16)]

        # Clouds and grass
        self.clouds, self.grass = [], []

        # Auxiliary that makes that in each screen appears a cloud and a grass
        aux = 0
        for i in range(8):
            x = random.randint(0, 256)
            x2 = random.randint(0, 256)
            y = random.randint(80, 100)
            self.clouds.append(Clouds(x + aux, y, 0, 16, 64, 48, 24, False))
            self.grass.append(Grass(x2 + aux, 224, 0, 16, 88, 48, 16, False))
            aux += 256

        # Pipes
        self.pipes = [Pipes(288, 208, 0, 32, 0, 32, 32, False),
                      Pipes(528, 208, 0, 32, 0, 32, 32, False),
                      Pipes(848, 208, 0, 32, 0, 32, 32, False),
                      Pipes(200, 176, 0, 0, 120, 32, 64, False),
                      Pipes(1408, 208, 0, 32, 0, 32, 32, False)
                      ]

        # Bricks with coins
        self.coin_bricks = [CoinBrick(64, 176, 0, 0, 16, 16, 16, True),
                            CoinBrick(96, 176, 0, 0, 16, 16, 16, True),
                            CoinBrick(608, 176, 0, 0, 16, 16, 16, True),
                            CoinBrick(1728, 176, 0, 0, 16, 16, 16, True),
                            CoinBrick(304, 176, 0, 0, 16, 16, 16, True),
                            CoinBrick(1744, 112, 0, 0, 16, 16, 16, True),
                            CoinBrick(1744, 160, 0, 0, 16, 16, 16, True)
                            ]

        # Breakable bricks
        self.breakable_bricks = [BreakableBrick(576, 176, 0, 0, 16, 16, 16, True),
                                 BreakableBrick(1408, 160, 0, 0, 16, 16, 16, True),
                                 BreakableBrick(1728, 112, 0, 0, 16, 16, 16, True),
                                 BreakableBrick(320, 176, 0, 0, 16, 16, 16, True),
                                 BreakableBrick(288, 141, 0, 0, 16, 16, 16, True)
                                 ]

        # Questions blocks_folder
        self.questions = [QuestionBlock(80, 176, 0, 16, 0, 16, 16, True),
                          QuestionBlock(1152, 176, 0, 16, 0, 16, 16, True),
                          QuestionBlock(1424, 112, 0, 16, 0, 16, 16, True)]

        self.flag = [Flag(2000, 88, 0, 224, 104, 32, 160, False)]

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

#######################################################################################################################
        # ENEMIES
        # Koopa Troopa
        self.koopa_troopa = [KoopaTroopa(736, 216, 0, 48, 32, 16, 24, True, False),
                             KoopaTroopa(1790, 216, 0, 48, 32, 16, 24, True, False)]
        # Goomba
        self.goomba = [Goomba(i * 256, 224, 0, 32, 48, 16, 16, True, False) for i in range(6) if i != 0 or i != 3 or i != 8]

        # List with all the enemies
        self.enemies = [self.koopa_troopa, self.goomba]

#######################################################################################################################
        # SPECIAL OBJECTS
        self.mushroom = [Mushroom(80, 157, 0, 0, 32, 16, 16, True),
                         Mushroom(1152, 157, 0, 0, 32, 16, 16, False),
                         Mushroom(1424, 93, 0, 0, 32, 16, 16, False)]

        self.coin = [Coin(64, 160, 0, 48, 120, 16, 16, True),
                     Coin(96, 160, 0, 48, 120, 16, 16, False),
                     Coin(608, 160, 0, 48, 120, 16, 16, False),
                     Coin(1728, 160, 0, 48, 120, 16, 16, False),
                     Coin(304, 160, 0, 48, 120, 16, 16, False),
                     Coin(1744, 96, 0, 48, 120, 16, 16, False),
                     Coin(1744, 144, 0, 48, 120, 16, 16, False)]

        self.special_objects = [self.mushroom, self.coin]


    def update(self):
        # Function is called each frame
        # Quit the game if you press Q or if Mario dies
        if pyxel.btn(pyxel.KEY_Q) or self.mario.state == 0 or self.mario.x+1 == self.blocks[7][0].x_position:
            pyxel.quit()

        # Return the value of hit, to give mario some time for the next attack
        if self.mario.hit<=150 and self.mario.hit>0:
            self.mario.hit-=1

        # States the sprite of mario
        self.mario.choose_sprite()

        # Decreases time
        self.game_time -= .07

        ###############################################################
        ##################### ENEMIES´S MOVEMENT ######################
        ###############################################################
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

        ###############################################################
        ##################### MARIO´S MOVEMENT ########################
        ###############################################################
        # Updates the next position of mario
        self.mario.update_next_move()

        # Mario's movement to the right
        if pyxel.btn(pyxel.KEY_RIGHT) and self.mario.x < (
                (self.width / 2) - 16) and self.mario.next_move_right not in self.blocks_x_y:
            self.mario.move_right()
            # print(self.mario.x_and_y_coordinates)

        # Mario would stop running to the right at the middle of the screen
        # Then the blocks would move to the left
        if pyxel.btn(pyxel.KEY_RIGHT) and self.mario.x == (
                (self.width / 2) - 16) and self.mario.next_move_right not in self.blocks_x_y:
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
                    for k in range(self.blocks[i][j].x_position,
                                   self.blocks[i][j].x_position + self.blocks[i][j].width + 1, 1):
                        for w in range(self.blocks[i][j].y_position,
                                       self.blocks[i][j].y_position + self.blocks[i][j].height + 1, 1):
                            self.blocks_x_y.append([k, w])

        # Mario's movement to the left
        if pyxel.btn(pyxel.KEY_LEFT) and self.mario.x - 1 > 0 and self.mario.next_move_left not in self.blocks_x_y:
            self.mario.move_left()

        # Mario´s jump
        if pyxel.btn(pyxel.KEY_UP) and self.mario.next_move_up not in self.blocks_x_y and self.mario.jump_height <= 70:
            self.mario.jump()
            # Breaks the blocks that has some function
            aux2 = []
            for i in range(3, len(self.blocks) - 1, 1):
                for j in range(len(self.blocks[i])):
                    aux = []
                    for k in range(self.blocks[i][j].x_position, self.blocks[i][j].x_position + self.blocks[i][j].width,
                                   1):
                        for w in range(self.blocks[i][j].y_position,
                                       self.blocks[i][j].y_position + self.blocks[i][j].height, 1):
                            aux.append([k, w])
                    aux2.append(aux)
                    if self.mario.next_move_up in aux[3]:
                        del (self.coin_bricks[3])
                        self.mario.increase_coins()

        # Gravity
        if self.mario.y <= 240 and \
                self.mario.next_move_down not in self.blocks_x_y and self.mario.jump_height > 70:
            self.mario.un_jump()

        # Regulate Mario's jumps
        if self.mario.next_move_down in self.blocks_x_y:
            self.mario.jump_height = 0

        if pyxel.btn(pyxel.KEY_UP) == False or self.mario.next_move_up in self.blocks_x_y:
            self.mario.jump_height = 71

        ###############################################################
        ##################### MARIO VS ENEMIES ########################
        ###############################################################

        # This loop goes through all the enemies_folder
        for i in range(len(self.enemies)):
            for j in range(len(self.enemies[i])):
                aux = []
                if not self.enemies[i][j].dead:
                    for k in range(self.enemies[i][j].x_position, self.enemies[i][j].x_position + self.enemies[i][j].width + 1, 1):
                        for w in range(self.enemies[i][j].y_position, self.enemies[i][j].y_position + self.enemies[i][j].height + 1, 1):
                            aux.append([k, w])

                if self.mario.next_move_down in aux:
                    self.enemies[i][j].dead = True
                    self.mario.increase_score(100)

                elif ([self.mario.x + 1, self.mario.y] in aux or [self.mario.x - 1, self.mario.y] in aux) and self.mario.hit == 0:
                    self.mario.hit = 150
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

        # Draw blocks
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                self.blocks[i][j].draw_block()

        # Draw enemies
        for i in range(len(self.enemies)):
            for j in range(len(self.enemies[i])):
                if not self.enemies[i][j].dead:
                    self.enemies[i][j].draw_enemy()

        # Draw Objects
        for i in range(len(self.special_objects)):
            for j in range(len(self.special_objects[i])):
                    self.special_objects[i][j].draw_special_object()

        # Draw Mario
        if self.mario.state == 1 or self.mario.state == 0:
            pyxel.blt(self.mario.x, self.mario.y - 17, 0, self.mario.animation_x, self.mario.animation_y,
                      self.mario.sprite_direction, 16, colkey=12)
        if self.mario.state == 2:
            pyxel.blt(self.mario.x, self.mario.y - 32, 0, self.mario.animation_x, self.mario.animation_y,
                      self.mario.sprite_direction, 32, colkey=12)

        """ Draw Mario
        pyxel.blt(self.mario.x, self.mario.y - 17, 0, self.mario.animation_x, self.mario.animation_y,
                  self.mario.sprite_direction, 16, colkey=12)"""
