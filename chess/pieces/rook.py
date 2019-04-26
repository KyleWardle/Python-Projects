from .piece import *


class Rook(Piece):
    def __init__(self, board, start_x, start_y, color='black'):
        super().__init__(board, start_x, start_y, color)
        self.letter = 'R'
        self.draw()

    def move_is_valid(self, move_x, move_y):
        return self.check_move(move_x, move_y)

    def check_move(self, move_x, move_y):
        if self.move_is_straight(move_x, move_y):
            return self.path_has_no_obstacles(move_x, move_y)
        else:
            return False

