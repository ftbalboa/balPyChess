from tkinter import *
from PIL import Image as Pil_image, ImageTk as Pil_imageTk

PIECES_COLORS = ['white', 'black']
PIECES_ORDER = ['Rook', 'Horse', 'Bishop', 'Queen', 'King', 'Bishop', 'Horse', 'Rook',
                'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn']
COL_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ROW_NAMES = ['1', '2', '3', '4', '5', '6', '7', '8']
B_SQUARES_COLOR ="#A9A9A9"
W_SQUARES_COLOR ="#EDEDED"

class Piece:
    def __init__(self, name, color, position):  # position in (row col)
        self.name = name
        self.color = color
        self.position = position
        self.fancy_position = [ROW_NAMES[self.position[0]], COL_NAMES[self.position[1]]]
        self.ifSelect = False

    def set_position(self, position):
        self.position = position
        self.fancy_position = [ROW_NAMES[self.position[0]], COL_NAMES[self.position[1]]]

    def get_piece_name(self):
        """Console prints piece name and color"""
        return f"{self.name} {self.color}"


class Board:
    """Creates and stocks pieces"""

    def __init__(self, gui):
        self.pieces = []
        self.board = []
        self.rows = 8
        self.cols = 8
        self.gui = gui
        self.offset_x = 12
        self.offset_y = 12
        self.side_size = 75
        for row in range(self.rows):
            for_append = []
            for col in range(self.cols):
                for_append.append(None)
            self.board.append(for_append)
        self.gui.add_show(url=f'assets/board.gif', priority=1,
                          position=(0, 0))
        self.__init_position()

    def __init_position(self):
        """Set initial position for pieces, store and create them"""
        for color in PIECES_COLORS:
            if color == "white":
                col = 0
                row = 0
                for name in PIECES_ORDER:
                    piece = Piece(name, color, (row, col))
                    self.gui.add_show(url=f'assets/{piece.color}{piece.name}.png', priority=1, position=self.board_pixel_position(row, col))
                    self.pieces.append(piece)
                    self.board[row][col] = self.pieces[len(self.pieces) - 1]
                    col += 1
                    if col == self.cols:
                        col = 0
                        row += 1
            if color == "black":
                row = self.rows - 1
                col = 0
                for name in PIECES_ORDER:
                    piece = Piece(name, color, (row, col))
                    self.gui.add_show(url=f'assets/{piece.color}{piece.name}.png', priority=1, position=self.board_pixel_position(row, col))
                    self.pieces.append(piece)
                    self.board[row][col] = self.pieces[len(self.pieces) - 1]
                    col += 1
                    if col == self.cols:
                        col = 0
                        row -= 1

    def print_pieces(self):
        """Console prints all pieces name color and position"""
        for piece in self.pieces:
            print(piece.get_piece_name())

    def print_board(self):
        """Prints on console full board"""
        for row in range(self.rows):
            for_append = ''
            for col in range(self.cols):
                if self.board[row][col] is None:
                    for_append += f' {self.board[row][col]}'
                else:
                    for_append += f' {self.board[row][col].get_piece_name()}'
            print(f'{ROW_NAMES[row]}{for_append}')
        print('   A    B    C    D    E    F    G    H  ')

    def board_pixel_position(self, row, col):
        return [row * self.side_size + self.offset_y, col * self.side_size + self.offset_x]


class Rules:
    def __init__(self, name, color, position):
        pass

    def is_check(self):
        pass

    def possible_movs(self):
        pass


class GamePanel:
    def __init__(self):
        self.start = False


class IA:
    def __init__(self):
        pass

    def next_move(self):
        pass


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("balPyChess")
        self.window.minsize(width=800, height=600)
        self.canvas = Canvas(bg="grey", width=800, height=600, highlightthickness=0,bd=0)
        self.canvas.place(x=0, y=0)
        self.for_show = []

    def startloop(self):
        self.window.mainloop()

    def set_bind(self, cb):
        self.canvas.bind("<Button-1>", cb)

    def add_show(self, url, priority, position):
        front_image = Pil_imageTk.PhotoImage(image=Pil_image.open(url))
        panel = Label(self.window, image=front_image)
        panel.config(bg=B_SQUARES_COLOR)
        panel.photo = front_image
        panel.place(y=position[0], x=position[1])
        self.for_show.append(panel)
