# balPyChess
import random
import pieces


# TODO:     Select piece
#           make callback function
#           match labels with pieces


VERSION = 0.001

board = pieces.Board()
gui = pieces.GUI(board)
rules = pieces.Rules(board)
gui.set_bind(rules.select_piece)


# def callback(event):
#     print("click")
#     uesa.place(x=100, y=100)

# ************** User Interface ************* #


# Main Loop
gui.startloop()
