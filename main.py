# balPyChess
import random
import pieces


# TODO:         make function "possible moves"


VERSION = 0.001

board = pieces.Board()
gui = pieces.GUI(board)
game = pieces.Game(gui, board)

# Start Loop
gui.startloop()
