import importlib
from graphics import *
from board import *

importlib.import_module("graphics")


class Application:
    def __init__(self, canvas_size, amount_of_squares=8):
        self.canvas_size = canvas_size
        self.board = None
        self.amount_of_squares = amount_of_squares
        self.turn = 'grey'

        window = GraphWin(width=500, height=500)  # create a window
        window.setCoords(0, 0, canvas_size, canvas_size)
        self.window = window

    def start(self):
        print("start")
        self.board = Board(self)

        while True:
            mouse = self.window.getMouse()
            coords = self.board.get_coords_from_point(mouse)
            print(str(coords['x']) + ', ' + str(coords['y']))
            selected_piece = self.board.positions[coords['x']][coords['y']]
            if selected_piece is not None and selected_piece.color == self.turn:
                print("Found piece")
                move_mouse = self.window.getMouse()
                move_coords = self.board.get_coords_from_point(move_mouse)

                move = selected_piece.move(move_coords['x'], move_coords['y'])

                if move:  # If move was valid
                    self.turn = 'black' if self.turn == 'grey' else 'grey'


# For rooks : One can be whatever whereas one has to be 0. Need to figure out if things are in way
# For Bishops : The difference of both have to be the same, need to figure out if things are in way
# Maybe do a for loop over the 'path' of the piece on each square?
def main():
    application = Application(1000)
    application.start()
    application.window.getMouse()


main()
