from .piece import *


class King(Piece):
    def __init__(self, board, start_x, start_y, color='black'):
        super().__init__(board, start_x, start_y, color)
        self.letter = 'K'
        self.draw()

    def move_is_one_place(self, move_x, move_y):
        diff_x = self.x - move_x
        diff_y = self.y - move_y
        return 1 >= diff_x >= -1 and 1 >= diff_y >= -1

    def move_is_valid(self, move_x, move_y):
        print(self.move_is_one_place(move_x, move_y))
        if self.move_is_one_place(move_x, move_y):
            return self.check_move(move_x, move_y)
        else:
            return False

    def check_move(self, move_x, move_y):
        if self.move_is_straight(move_x, move_y) or self.move_is_diagonal(move_x, move_y):
            return self.path_has_no_obstacles(move_x, move_y)
        else:
            return False

