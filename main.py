# balPyChess
import random
import pieces


# TODO:         in function "possible moves"
#                   add al paso threats for pawn
#               add function move
#               add function eat


VERSION = 0.001

board = pieces.Board()
gui = pieces.GUI(board)
game = pieces.Game(gui, board)

# Start Loop
gui.startloop()
