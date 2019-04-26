from .piece import *


class Rook(Piece):
    def __init__(self, board, start_x, start_y, color='black'):
        super().__init__(board, start_x, start_y, color)
        self.letter = 'R'
        self.draw()

    def move_is_valid(self, move_x, move_y):
        return self.check_move(move_x, move_y)

    def move_is_straight(self, move_x, move_y):
        diff_x = self.x - move_x
        diff_y = self.y - move_y

        return diff_x == 0 or diff_y == 0

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
                if not(destination_piece and not_own_piece):
                    return False

        return True

    def check_move(self, move_x, move_y):
        if self.move_is_straight(move_x, move_y):
            if self.path_has_no_obstacles(move_x, move_y):
                return True
            else:
                return False
        else:
            return False

