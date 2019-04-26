

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

    @staticmethod
    def calculate_increment(diff):
        if diff < 0:
            return 1
        elif diff > 0:
            return -1
        else:
            return 0

    def path_has_no_obstacles(self, move_x, move_y):
        diff_x = self.x - move_x
        diff_y = self.y - move_y
        print('diff', diff_x, diff_y)

        temp_x = self.x
        temp_y = self.y
        print('temp', temp_x, temp_y)

        x_increment = self.calculate_increment(diff_x)
        y_increment = self.calculate_increment(diff_y)
        print('increment', x_increment, y_increment)

        largest_count = abs(diff_x) if abs(diff_x) > abs(diff_y) else abs(diff_y)
        # can use diff_x or diff_y as should have same result
        for i in range(0, largest_count):
            temp_x += x_increment
            temp_y += y_increment

            print('temps', temp_x, temp_y)
            target = self.board.positions[temp_x][temp_y]

            if target is not None:
                print("found target")
                not_own_piece = target.color != self.color
                destination_piece = i == abs(largest_count) - 1
                print('own', not_own_piece, 'destin', destination_piece)
                if not (destination_piece and not_own_piece):
                    return False

        return True

    def move_is_straight(self, move_x, move_y):
        diff_x = self.x - move_x
        diff_y = self.y - move_y
        return diff_x == 0 or diff_y == 0

    def move_is_diagonal(self, move_x, move_y):
        diff_x = self.x - move_x
        diff_y = self.y - move_y
        return abs(diff_x) == abs(diff_y)