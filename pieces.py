from tkinter import *
from PIL import Image as Pil_image, ImageTk as Pil_imageTk

PIECES_COLORS = ['white', 'black']
PIECES_ORDER = ['Rook', 'Horse', 'Bishop', 'Queen', 'King', 'Bishop', 'Horse', 'Rook',
                'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn']
COL_NAMES = ['H', 'G', 'C', 'E', 'D', 'C', 'B', 'A']
ROW_NAMES = ['1', '2', '3', '4', '5', '6', '7', '8']
B_SQUARES_COLOR = "#A9A9A9"
W_SQUARES_COLOR = "#EDEDED"
IMG_SELECT = 'assets/select.png'
IMG_MOV = 'assets/posMove.png'

class Piece:
    def __init__(self, name, color, position):  # position in (row col)
        self.name = name
        self.color = color
        self.position = position
        self.fancy_position = [ROW_NAMES[self.position[0]], COL_NAMES[self.position[1]]]
        self.if_select = False
        self.offset = 12
        self.label = ""

    def set_position(self, position):
        self.position = position
        self.fancy_position = [ROW_NAMES[self.position[0]], COL_NAMES[self.position[1]]]

    def get_piece_name(self):
        """Console prints piece name and color"""
        return f"{self.name} {self.color}"

    def get_position(self):
        return self.position

    def set_select(self, select):
        self.if_select = select

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label

    def get_if_select(self):
        return self.if_select

    def set_if_select(self, select):
        self.if_select = select

    def get_color(self):
        return self.color


class Board:
    """Creates and stocks pieces"""

    def __init__(self):
        self.pieces = []
        self.board = []
        self.rows = 8
        self.cols = 8
        self.offset_x = 12
        self.offset_y = 12
        self.side_size = 75
        self.label = []
        for row in range(self.rows):
            for_append = []
            for col in range(self.cols):
                for_append.append(None)
            self.board.append(for_append)
        self.__init_position()

    def __init_position(self):
        """Set initial position for pieces, store and create them"""
        for color in PIECES_COLORS:
            if color == "white":
                col = 0
                row = self.rows - 1
                for name in PIECES_ORDER:
                    piece = Piece(name, color, (row, col))
                    self.pieces.append(piece)
                    self.board[row][col] = self.pieces[len(self.pieces) - 1]
                    col += 1
                    if col == self.cols:
                        col = 0
                        row -= 1
            if color == "black":
                row = 0
                col = 0
                for name in PIECES_ORDER:
                    piece = Piece(name, color, (row, col))
                    self.pieces.append(piece)
                    self.board[row][col] = self.pieces[len(self.pieces) - 1]
                    col += 1
                    if col == self.cols:
                        col = 0
                        row += 1

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

    def board_pixel_position(self, pos):
        return [pos[0] * self.side_size + self.offset_y, pos[1] * self.side_size + self.offset_x]

    def get_board(self):
        return self.board

    def get_square_color(self, pos):
        row = pos[0]
        col = pos[1]
        if row % 2 == 0:
            pos = col + 1
        else:
            pos = col
        if pos % 2 == 0:
            return B_SQUARES_COLOR
        else:
            return W_SQUARES_COLOR

    def get_square(self, pixels):
        col = pixels[0]
        row = pixels[1]
        col = col // self.side_size
        row = row // self.side_size
        return [col, row]

    def get_pieces(self):
        return self.pieces

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label


class Game:
    def __init__(self, gui, board):
        self.gui = gui
        self.board = board
        self.selected = False
        self.turn = PIECES_COLORS[0]
        self.gui.set_bind(self.select_piece)
        self.select_item = Items("select", (0, 0))
        self.select_item.set_label(self.gui.add_show(IMG_SELECT, 2, (0, 0)))
        self.gui.hide_label(self.select_item.get_label())

    def is_check(self):
        pass

    def possible_movs(self):
        pass

    def select_piece(self, event):
        if self.board.get_label() is event.widget:
            pass
        else:
            for piece in self.board.get_pieces():
                if piece.get_label() is event.widget:
                    if piece.get_color() is self.turn:
                        self.deselect_all()
                        piece.set_if_select(True)
                        self.selected = True
                        self.gui.place_label(self.select_item.get_label(), piece.get_position())
                        print(piece.name)

    def deselect_all(self):
        for piece in self.board.get_pieces():
            piece.set_if_select(False)


class IA:
    def __init__(self):
        pass

    def next_move(self):
        pass


class Items:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.label = ""

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label


class GUI:
    def __init__(self, board, board_x=0, board_y=0, board_square=75):
        self.window = Tk()
        self.window.title("balPyChess")
        self.window.minsize(width=800, height=600)
        self.canvas = Canvas(bg="grey", width=800, height=600, highlightthickness=0, bd=0)
        self.canvas.place(x=0, y=0)
        self.board = board
        self.board_x = board_x
        self.board_y = board_y
        self.board_square = board_square
        self.charge_board()

    def startloop(self):
        self.window.mainloop()

    def set_bind(self, cb):
        self.window.bind("<Button-1>", cb)

    def add_show(self, url, priority, position, square_color='white'):
        front_image = Pil_imageTk.PhotoImage(image=Pil_image.open(url))
        panel = Label(self.window, image=front_image)
        panel.config(bg=square_color)
        panel.photo = front_image
        panel.place(y=position[0], x=position[1])
        return panel

    def charge_board(self):
        self.board.set_label(self.add_show(url=f'assets/board.gif', priority=0, position=(0, 0)))
        for row in self.board.get_board():
            for piece in row:
                if piece is not None:
                    piece.set_label(self.add_show(url=f'assets/{piece.color}{piece.name}.png', priority=1,
                                                  position=self.board.board_pixel_position(piece.get_position()),
                                                  square_color=self.board.get_square_color(piece.get_position())))

    def hide_label(self, label):
        label.place_forget()

    def place_label(self, label, position):
        label.place(y=position[0], x=position[1])