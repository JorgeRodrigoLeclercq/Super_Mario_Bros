import pyxel
from board import Board

# Basic information
width = 256
height = 256
floor_length = 2176

# Creates the screen
pyxel.init(width, height, caption="MarioBros")

# Loads the assets
pyxel.load("assets\marioassets.pyxres")

# Execute the board
mario_board = Board(width, height, floor_length)
pyxel.run(mario_board.update, mario_board.draw)
