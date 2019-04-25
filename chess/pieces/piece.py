

import importlib
from graphics import *

importlib.import_module("graphics")


class Piece:
    def __init__(self, board, start_x, start_y, color='black'):
        self.board = board
        self.letter = "X"
        self.color = color
        self.text = None
        self.x = None
        self.y = None
        self.move_count = 0
        self.setup_start_positions(start_x, start_y)

    def draw(self):
        coords = self.board.get_coords(self.x, self.y)
        point = Point(coords['x'], coords['y'])

        if self.text is not None:
            self.text.undraw()
        self.text = Text(point, self.letter)
        self.text.setOutline(self.color)
        self.text.draw(self.board.application.window)

    def move(self, move_x, move_y):
        if self.move_is_valid(move_x, move_y):
            self.move_count += 1
            own_coords = self.board.get_coords(self.x, self.y)
            new_coords = self.board.get_coords(move_x, move_y)

            diff_x = new_coords['x'] - own_coords['x']
            diff_y = new_coords['y'] - own_coords['y']

            self.text.move(diff_x, diff_y)

            self.board.positions[self.x][self.y] = None
            self.x = move_x
            self.y = move_y

            previous_piece = self.board.positions[self.x][self.y]
            if previous_piece is not None:
                previous_piece.text.undraw()

            self.board.positions[self.x][self.y] = self

    def move_is_valid(self, move_x, move_y):
        if self.board.positions[move_x][move_y] is None:
            return True
        else:
            return False

    def setup_start_positions(self, start_x, start_y):
        if self.board.positions[start_x][start_y] is None:
            self.x = start_x
            self.y = start_y
            self.board.positions[start_x][start_y] = self
            self.draw()
        else:
            raise Exception
