from .piece import *


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
