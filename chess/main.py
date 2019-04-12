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


class Board:
    def __init__(self, application):
        self.application = application
        self.create_board()

    def create_board(self):
        self.create_outline()
        self.create_squares()
        self.create_keys()

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
            top_right_corner = Point(remaining_canvas_left + canvas_5_percent,second_point_coord)
            line = Rectangle(bottom_left_corner, top_right_corner)
            line.draw(self.application.window)

    def create_keys(self):
        canvas_5_percent = (self.application.canvas_size / 100) * 5
        canvas_10_percent = canvas_5_percent * 2
        remaining_canvas_left = self.application.canvas_size - canvas_10_percent

        section_length = remaining_canvas_left / self.application.amount_of_squares

        letters_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(1, self.application.amount_of_squares + 1):
            text_location = Point(canvas_5_percent / 2, (section_length * i))
            text = Text(text_location, letters_arr[i - 1])
            text.draw(self.application.window)

        numbers_array = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in range(1, self.application.amount_of_squares + 1):
            text_location = Point((section_length * i), canvas_5_percent / 2)
            text = Text(text_location, numbers_array[i - 1])
            text.draw(self.application.window)

    def get_coords(self, x, y):


def main():
    application = Application(1000)
    application.start()
    application.window.getMouse()


main()
