# balPyChess
import random
import pieces


# TODO:   Show in display

VERSION = 0.001

gui = pieces.GUI()
board = pieces.Board(gui)
board.print_board()

# def callback(event):
#     print("click")
#     uesa.place(x=100, y=100)

# ************** User Interface ************* #


# Main Loop
gui.startloop()
