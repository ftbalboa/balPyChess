# balPyChess
import random
import pieces


# TODO:     place selection (using square's color, priority and pixel position)
#           make function "possible moves"


VERSION = 0.001

board = pieces.Board()
gui = pieces.GUI(board)
game = pieces.Game(gui, board)



# def callback(event):
#     print("click")
#     uesa.place(x=100, y=100)

# ************** User Interface ************* #


# Main Loop
gui.startloop()
