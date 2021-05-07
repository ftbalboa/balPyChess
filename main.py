# balPyChess
import tkinter
import random
import pieces

# TODO:   1-Pieces class
#         2-Rules class
#         3-GamePanel class
#         4-Board class
#         5-IA class


VERSION = 0.001

board = pieces.Board()
board.print_pieces()

# ************** User Interface ************* #
window = tkinter.Tk()
window.title("balPyChess")
window.minsize(width=800, height=600)
canvas = tkinter.Canvas(bg="grey", width=800, height=600, highlightthickness=0)
canvas.place(x=0, y=0)

front_image = tkinter.PhotoImage(file='assets/board.png')
canvas.create_image(450, 300, image=front_image)

# Main Loop
window.mainloop()
