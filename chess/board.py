import math
from pieces.piece import *
from pieces.pawn import *
from pieces.bishop import *
from pieces.rook import *
from pieces.queen import *
from pieces.king import *

class Board:
    def __init__(self, application):
        self.application = application
        self.positions = self.create_positions()
        self.five_percent = (self.application.canvas_size / 100) * 5
        self.create_board()

    def create_board(self):
        self.create_outline()
        self.create_squares()
        self.create_keys()
        self.create_pieces()

    def create_outline(self):
        canvas_95_percent = self.application.canvas_size - self.five_percent

        bottom_left_corner = Point(self.five_percent, self.five_percent)
        top_right_corner = Point(canvas_95_percent, canvas_95_percent)

        rectangle = Rectangle(bottom_left_corner, top_right_corner)
        rectangle.draw(self.application.window)

    def get_coords_from_point(self, mouse):
        canvas_10_percent = self.five_percent * 2
        remaining_canvas_left = self.application.canvas_size - canvas_10_percent

        section_length = remaining_canvas_left / self.application.amount_of_squares

        return {
            'x': int(math.floor((mouse.getX() - self.five_percent) / section_length)) + 1,
            'y': int(math.floor((mouse.getY() - self.five_percent) / section_length)) + 1
        }

    def create_squares(self):
        canvas_10_percent = self.five_percent * 2
        remaining_canvas_left = self.application.canvas_size - canvas_10_percent

        section_length = remaining_canvas_left / self.application.amount_of_squares

        for i in range(0, self.application.amount_of_squares):
            first_point_coord = (i * section_length) + self.five_percent
            second_point_coord = ((i + 1) * section_length) + self.five_percent

            bottom_left_corner = Point(first_point_coord, self.five_percent)
            top_right_corner = Point(second_point_coord, remaining_canvas_left + self.five_percent)
            line = Rectangle(bottom_left_corner, top_right_corner)
            line.draw(self.application.window)

        for i in range(0, self.application.amount_of_squares):
            first_point_coord = (i * section_length) + self.five_percent
            second_point_coord = ((i + 1) * section_length) + self.five_percent

            bottom_left_corner = Point(self.five_percent, first_point_coord)
            top_right_corner = Point(remaining_canvas_left + self.five_percent, second_point_coord)
            line = Rectangle(bottom_left_corner, top_right_corner)
            line.draw(self.application.window)

    def create_keys(self):
        remaining_canvas_left = self.application.canvas_size - self.five_percent * 2

        section_length = remaining_canvas_left / self.application.amount_of_squares

        numbers_array = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in range(1, self.application.amount_of_squares + 1):
            text_location = Point(self.five_percent / 2, (section_length * i))
            text = Text(text_location, numbers_array[i - 1])
            text.draw(self.application.window)

        for i in range(1, self.application.amount_of_squares + 1):
            text_location = Point((section_length * i), self.five_percent / 2)
            text = Text(text_location, numbers_array[i - 1])
            text.draw(self.application.window)

    @staticmethod
    def create_positions():
        return {
            1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
            2: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
            3: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
            4: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
            5: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
            6: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
            7: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
            8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}
        }

    def get_coords(self, x, y):
        remaining_canvas_left = self.application.canvas_size - self.five_percent * 2

        section_length = remaining_canvas_left / self.application.amount_of_squares

        return {
            'x': self.five_percent + (section_length * x) - (section_length / 2),
            'y': self.five_percent + (section_length * y - (section_length / 2))
        }

    def create_pieces(self):
        self.create_white_pieces()
        self.create_black_pieces()

    def create_white_pieces(self):
        Rook(self, 1, 8, 'grey')
        Piece(self, 2, 8, 'grey')
        Bishop(self, 3, 8, 'grey')
        King(self, 4, 8, 'grey')
        Queen(self, 5, 8, 'grey')
        Bishop(self, 6, 8, 'grey')
        Piece(self, 7, 8, 'grey')
        Rook(self, 8, 8, 'grey')

        Pawn(self, 1, 7, 'grey')
        Pawn(self, 2, 7, 'grey')
        Pawn(self, 3, 7, 'grey')
        Pawn(self, 4, 7, 'grey')
        Pawn(self, 5, 7, 'grey')
        Pawn(self, 6, 7, 'grey')
        Pawn(self, 7, 7, 'grey')
        Pawn(self, 8, 7, 'grey')

    def create_black_pieces(self):
        Rook(self, 1, 1)
        Piece(self, 2, 1)
        Bishop(self, 3, 1)
        Queen(self, 4, 1)
        King(self, 5, 1)
        Bishop(self, 6, 1)
        Piece(self, 7, 1)
        Rook(self, 8, 1)

        Pawn(self, 1, 2)
        Pawn(self, 2, 2)
        Pawn(self, 3, 2)
        Pawn(self, 4, 2)
        Pawn(self, 5, 2)
        Pawn(self, 6, 2)
        Pawn(self, 7, 2)
        Pawn(self, 8, 2)
