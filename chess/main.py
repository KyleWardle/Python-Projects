import importlib
from graphics import *
import math

importlib.import_module("graphics")


class Application:
    def __init__(self, canvas_size, amount_of_squares=8):
        self.canvas_size = canvas_size
        self.board = None
        self.amount_of_squares = amount_of_squares

        window = GraphWin(width=1000, height=1000)  # create a window
        window.setCoords(0, 0, canvas_size, canvas_size)
        self.window = window

    def start(self):
        print("start")
        self.board = Board(self)
        piece = self.board.positions[1][2]

        while True:
            mouse = self.window.getMouse()
            coords = self.board.get_coords_from_point(mouse)
            print(str(coords['x']) + ', ' + str(coords['y']))
            selected_piece = self.board.positions[coords['x']][coords['y']]
            if selected_piece is not None:
                print("Found piece")
                move_mouse = self.window.getMouse()
                move_coords = self.board.get_coords_from_point(move_mouse)

                selected_piece.move(move_coords['x'], move_coords['y'])


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
        Piece(self, 1, 8, 'grey')
        Piece(self, 2, 8, 'grey')
        Piece(self, 3, 8, 'grey')
        Piece(self, 4, 8, 'grey')
        Piece(self, 5, 8, 'grey')
        Piece(self, 6, 8, 'grey')
        Piece(self, 7, 8, 'grey')
        Piece(self, 8, 8, 'grey')

        Pawn(self, 1, 7, 'grey')
        Pawn(self, 2, 7, 'grey')
        Pawn(self, 3, 7, 'grey')
        Pawn(self, 4, 7, 'grey')
        Pawn(self, 5, 7, 'grey')
        Pawn(self, 6, 7, 'grey')
        Pawn(self, 7, 7, 'grey')
        Pawn(self, 8, 7, 'grey')

    def create_black_pieces(self):
        Piece(self, 1, 1)
        Piece(self, 2, 1)
        Piece(self, 3, 1)
        Piece(self, 4, 1)
        Piece(self, 5, 1)
        Piece(self, 6, 1)
        Piece(self, 7, 1)
        Piece(self, 8, 1)

        Pawn(self, 1, 2)
        Pawn(self, 2, 2)
        Pawn(self, 3, 2)
        Pawn(self, 4, 2)
        Pawn(self, 5, 2)
        Pawn(self, 6, 2)
        Pawn(self, 7, 2)
        Pawn(self, 8, 2)


class Piece:
    def __init__(self, board, start_x, start_y, color='black'):
        self.board = board
        self.letter = "X"
        self.color = color
        self.text = None
        self.x = None
        self.y = None
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


class Pawn(Piece):
    def __init__(self, board, start_x, start_y, color='black'):
        super().__init__(board, start_x, start_y, color)
        self.letter = 'P'
        self.draw()
        self.move_count = 0

    def move_is_valid(self, move_x, move_y):
        return self.check_move(move_x, move_y)

    def move_is_forward(self, move_x, move_y):
        if self.color == 'grey':
            return (move_y < self.y) and (move_x == self.x)
        else:
            return (move_y > self.y) and (move_x == self.x)

    def move_is_diagonal(self, move_x, move_y):
        if self.color == 'grey':
            return ((move_x - 1 == self.x) and (move_y + 1 == self.y)) or (
                    (move_x + 1 == self.x) and (move_y + 1 == self.y))
        else:
            return ((move_x - 1 == self.x) and (move_y - 1 == self.y)) or (
                    (move_x + 1 == self.x) and (move_y - 1 == self.y))

    def calculate_squares_moved_forward(self, move_y):
        if self.color == 'grey':
            return self.y - move_y
        else:
            return move_y - self.y

    def check_move(self, move_x, move_y):
        target = self.board.positions[move_x][move_y]
        if target is None:
            if self.move_is_forward(move_x, move_y):
                squares_moved_forward = self.calculate_squares_moved_forward(move_y)
                print(squares_moved_forward)
                if squares_moved_forward == 1:
                    self.move_count += 1
                    return True
                elif (squares_moved_forward == 2) and (self.move_count == 0):
                    self.move_count += 1
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.move_is_diagonal(move_x, move_y) and target.color != self.color:
                self.move_count += 1
                return True
            else:
                return False


# For rooks : One can be whatever whereas one has to be 0. Need to figure out if things are in way
# For Bishops : The difference of both have to be the same, need to figure out if things are in way
# Maybe do a for loop over the 'path' of the piece on each square?
def main():
    application = Application(1000)
    application.start()
    application.window.getMouse()


main()
