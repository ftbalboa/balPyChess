# balPyChess
import random
import pieces


# TODO:         make function "possible moves"
#                   add two squares pawn move
#                   add "infinite" moves
#                   add same color pieces as limitants
#                   add threats
#                   add exclusions for pawns
#                   add al paso threats for pawn
#                   return dicc with threats and moves


VERSION = 0.001

board = pieces.Board()
gui = pieces.GUI(board)
game = pieces.Game(gui, board)

# Start Loop
gui.startloop()
