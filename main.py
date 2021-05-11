# balPyChess
import random
import pieces


# TODO:     Select piece
#           make callback function


VERSION = 0.001

board = pieces.Board()
gui = pieces.GUI(board)



# def callback(event):
#     print("click")
#     uesa.place(x=100, y=100)

# ************** User Interface ************* #


# Main Loop
gui.startloop()
