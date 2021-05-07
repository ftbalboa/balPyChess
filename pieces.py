PIECES_COLORS = ['white', 'black']
PIECES_ORDER = ['rook', 'horse', 'bishop', 'queen', 'king', 'bishop', 'horse', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
COL_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ROW_NAMES = ['1', '2', '3', '4', '5', '6', '7', '8']


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

    def print_piece_name(self):
        """Console prints piece name color and position"""
        print(f"{self.name} {self.color} {self.fancy_position[0]} {self.fancy_position[1]}")


class Board:
    """Creates and stocks pieces"""

    def __init__(self):
        self.pieces = []
        self.board = []
        self.rows = 8
        self.cols = 8
        for row in range(self.rows):
            for_append =[]
            for col in range(self.col):
                for_append.append(None)
            self.board.append(for_append)

        self.__init_position()

    def __init_position(self):
        for color in PIECES_COLORS:
            if color == "white":
                col = 0
                row = 0
                for name in PIECES_ORDER:
                    self.pieces.append(Piece(name, color, (row, col)))
                    col += 1
                    if col == self.cols:
                        col = 0
                        row += 1
            if color == "black":
                row = self.rows - 1
                col = 0
                for name in PIECES_ORDER:
                    self.pieces.append(Piece(name, color, (row, col)))
                    col += 1
                    if col == self.cols:
                        col = 0
                        row -= 1

    def print_pieces(self):
        """Console prints all pieces name color and position"""
        for piece in self.pieces:
            piece.print_piece_name()

    def print_board(self):
        for row in range(self.rows):
            for_append = ''
            for col in range(self.cols):
                for_append(f' {self.board[row[col]]}')
                print(f'{ROW_NAMES[row]}{for_append}')
        print(' A B C D E F G H')

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
