from pygame import *

screen = display.set_mode((600, 600))


class Piece:

    def __new__(cls, colour, position):
        obj = screen.blit(colour, position)

        return obj

    def __init__(self, colour, position):
        self.colour = colour
        self.position = position


class Pawn(Piece):

    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.colour = colour
        self.position = position


class Bishop(Piece):

    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.colour = colour
        self.position = position


class Knight(Piece):

    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.colour = colour
        self.position = position


class Rook(Piece):

    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.colour = colour
        self.position = position


class Queen(Piece):

    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.colour = colour
        self.position = position


class King(Piece):

    def __init__(self, colour, position):
        super().__init__(colour, position)
        self.colour = colour
        self.position = position