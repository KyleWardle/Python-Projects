import importlib
from graphics import *

importlib.import_module("graphics")


class Application:
    def __init__(self, canvas_size, amount_of_squares=8):
        self.canvas_size = canvas_size
        self.board = None
        self.amount_of_squares = amount_of_squares

        window = GraphWin(width=400, height=400)  # create a window
        window.setCoords(0, 0, canvas_size, canvas_size)
        self.window = window

    def start(self):
        print("start")
        self.board = Board(self)
        piece = self.board.positions[1][2]

        while True:
            console_input = input('Enter a reference: ')
            if len(console_input) == 2:
                x = int(console_input[0])
                y = int(console_input[1])
                piece.move(x, y)


class Board:
    def __init__(self, application):
        self.application = application
        self.positions = self.create_positions()
        self.create_board()

    def create_board(self):
        self.create_outline()
        self.create_squares()
        self.create_keys()
        self.create_pieces()

    def create_outline(self):
        canvas_5_percent = (self.application.canvas_size / 100) * 5
        canvas_95_percent = self.application.canvas_size - canvas_5_percent

        bottom_left_corner = Point(canvas_5_percent, canvas_5_percent)
        top_right_corner = Point(canvas_95_percent, canvas_95_percent)

        rectangle = Rectangle(bottom_left_corner, top_right_corner)
        rectangle.draw(self.application.window)

    def create_squares(self):
        canvas_5_percent = (self.application.canvas_size / 100) * 5
        canvas_10_percent = canvas_5_percent * 2
        remaining_canvas_left = self.application.canvas_size - canvas_10_percent

        section_length = remaining_canvas_left / self.application.amount_of_squares

        for i in range(0, self.application.amount_of_squares):
            first_point_coord = (i * section_length) + canvas_5_percent
            second_point_coord = ((i + 1) * section_length) + canvas_5_percent

            bottom_left_corner = Point(first_point_coord, canvas_5_percent)
            top_right_corner = Point(second_point_coord, remaining_canvas_left + canvas_5_percent)
            line = Rectangle(bottom_left_corner, top_right_corner)
            line.draw(self.application.window)

        for i in range(0, self.application.amount_of_squares):
            first_point_coord = (i * section_length) + canvas_5_percent
            second_point_coord = ((i + 1) * section_length) + canvas_5_percent

            bottom_left_corner = Point(canvas_5_percent, first_point_coord)
            top_right_corner = Point(remaining_canvas_left + canvas_5_percent, second_point_coord)
            line = Rectangle(bottom_left_corner, top_right_corner)
            line.draw(self.application.window)

    def create_keys(self):
        canvas_5_percent = (self.application.canvas_size / 100) * 5
        canvas_10_percent = canvas_5_percent * 2
        remaining_canvas_left = self.application.canvas_size - canvas_10_percent

        section_length = remaining_canvas_left / self.application.amount_of_squares

        numbers_array = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in range(1, self.application.amount_of_squares + 1):
            text_location = Point(canvas_5_percent / 2, (section_length * i))
            text = Text(text_location, numbers_array[i - 1])
            text.draw(self.application.window)

        for i in range(1, self.application.amount_of_squares + 1):
            text_location = Point((section_length * i), canvas_5_percent / 2)
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
        canvas_5_percent = (self.application.canvas_size / 100) * 5
        canvas_10_percent = canvas_5_percent * 2
        remaining_canvas_left = self.application.canvas_size - canvas_10_percent

        section_length = remaining_canvas_left / self.application.amount_of_squares

        return_dict = {
            'x': canvas_5_percent + (section_length * x) - (section_length / 2),
            'y': canvas_5_percent + (section_length * y - (section_length / 2))
        }

        return return_dict

    def create_pieces(self):
        piece = Piece(self, 1, 2)
        piece2 = Piece(self, 2, 2)


class Piece:
    def __init__(self, board, start_x, start_y):
        self.board = board
        self.letter = "X"
        self.text = None
        if board.positions[start_x][start_y] is None:
            self.x = start_x
            self.y = start_y
            board.positions[start_x][start_y] = self
            self.draw()
        else:
            raise Exception

    def draw(self):
        coords = self.board.get_coords(self.x, self.y)
        point = Point(coords['x'], coords['y'])
        self.text = Text(point, self.letter)
        self.text.draw(self.board.application.window)

    def move(self, move_x, move_y):
        if self.move_is_valid(move_x, move_y):
            own_coords = self.board.get_coords(self.x, self.y)
            new_coords = self.board.get_coords(move_x, move_y)

            diff_x = new_coords['x'] - own_coords['x']
            diff_y = new_coords['y'] - own_coords['y']

            self.text.move(diff_x, diff_y)

            self.board.positions[self.x][self.y] = None

            self.x = move_x
            self.y = move_y

            self.board.positions[self.x][self.y] = self

    def move_is_valid(self, move_x, move_y):
        if self.board.positions[move_x][move_y] is None:
            return True
        else:
            return False


def main():
    application = Application(1000)
    application.start()
    application.window.getMouse()


main()
