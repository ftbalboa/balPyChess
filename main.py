# balPyChess
import random
import pieces


# TODO:     Change bg color of the pieces
#           Gui recives board and update displays (now its backwards)
#           Handle change of bg piece colors


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
