from .piece import *


class Knight(Piece):
    def __init__(self, board, start_x, start_y, color='black'):
        super().__init__(board, start_x, start_y, color)
        self.letter = 'Kn'
        self.draw()

    def move_is_valid(self, move_x, move_y):
        return self.check_move(move_x, move_y)

    def move_is_knight(self, move_x, move_y):
        diff_x = self.x - move_x
        diff_y = self.y - move_y

        larger_diff = abs(diff_x) if abs(diff_x) > abs(diff_y) else abs(diff_y)
        smaller_diff = abs(diff_y) if abs(diff_x) > abs(diff_y) else abs(diff_x)

        print(larger_diff, smaller_diff)
        return larger_diff == 2 and smaller_diff == 1

    def target_is_clear(self, move_x, move_y):
        target = self.board.positions[move_x][move_y]
        if target is None:
            return True
        else:
            return target.color != self.color

    def check_move(self, move_x, move_y):
        if self.move_is_knight(move_x, move_y):
            return self.target_is_clear(move_x, move_y)
        else:
            return False

