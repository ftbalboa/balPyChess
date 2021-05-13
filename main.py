# balPyChess
import random
import pieces


# TODO:     Add images for "piece select", "possible move" and "piece in danger"
#           make function "possible moves"


VERSION = 0.001

board = pieces.Board()
gui = pieces.GUI(board)
game = pieces.Game(board)
gui.set_bind(game.select_piece)


# def callback(event):
#     print("click")
#     uesa.place(x=100, y=100)

# ************** User Interface ************* #


# Main Loop
gui.startloop()
