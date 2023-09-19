from pygame import *

size = 75
# rows and columns
r_1 = 525
r_2 = 450
r_3 = 375
r_4 = 300
r_5 = 225
r_6 = 150
r_7 = 75
r_8 = 0

c_a = 0
c_b = 75
c_c = 150
c_d = 225
c_e = 300
c_f = 375
c_g = 450
c_h = 525

# board positions
a1, a2, a3, a4, a5, a6, a7, a8, \
b1, b2, b3, b4, b5, b6, b7, b8, \
c1, c2, c3, c4, c5, c6, c7, c8, \
d1, d2, d3, d4, d5, d6, d7, d8, \
e1, e2, e3, e4, e5, e6, e7, e8, \
f1, f2, f3, f4, f5, f6, f7, f8, \
g1, g2, g3, g4, g5, g6, g7, g8, \
h1, h2, h3, h4, h5, h6, h7, h8, = (c_a, r_1), (c_a, r_2), (c_a, r_3), (c_a, r_4), (c_a, r_5), (c_a, r_6), (c_a, r_7), \
                                  (c_a, r_8), (c_b, r_1), (c_b, r_2), (c_b, r_3), (c_b, r_4), (c_b, r_5), (c_b, r_6), (
                                      c_b, r_7), \
                                  (c_b, r_8), (c_c, r_1), (c_c, r_2), (c_c, r_3), (c_c, r_4), (c_c, r_5), (c_c, r_6), (
                                      c_c, r_7), \
                                  (c_c, r_8), (c_d, r_1), (c_d, r_2), (c_d, r_3), (c_d, r_4), (c_d, r_5), (c_d, r_6), (
                                      c_d, r_7), \
                                  (c_d, r_8), (c_e, r_1), (c_e, r_2), (c_e, r_3), (c_e, r_4), (c_e, r_5), (c_e, r_6), (
                                      c_e, r_7), \
                                  (c_e, r_8), (c_f, r_1), (c_f, r_2), (c_f, r_3), (c_f, r_4), (c_f, r_5), (c_f, r_6), (
                                      c_f, r_7), \
                                  (c_f, r_8), (c_g, r_1), (c_g, r_2), (c_g, r_3), (c_g, r_4), (c_g, r_5), (c_g, r_6), (
                                      c_g, r_7), \
                                  (c_g, r_8), (c_h, r_1), (c_h, r_2), (c_h, r_3), (c_h, r_4), (c_h, r_5), (c_h, r_6), (
                                      c_h, r_7), \
                                  (c_h, r_8)


class Game:
    def __init__(self):
        self.create_chess_board()

    def create_chess_board(self):
        # Define the size of the chess board
        board_size = (600, 600)

        # Create a surface object to represent the chess board
        chess_board = Surface(board_size)

        # Define the colors for the chess board
        green = (118, 150, 86)
        light_green = (238, 238, 210)

        # Define the size of each square on the chess board
        square_size = board_size[0] // 8

        # Define the letters for the columns
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        # Initialize a list to keep track of whether each tile is occupied
        is_occupied = [[False for _ in range(8)] for _ in range(8)]

        # Loop through each square on the chess board
        for row in range(8):
            for col in range(8):
                # Calculate the position of the square
                x = col * square_size
                y = row * square_size

                # Determine the color of the square based on its position
                if (row + col) % 2 == 0:
                    colour = green
                else:
                    colour = light_green

                # Draw the square on the chess board
                draw.rect(chess_board, colour, (x, y, square_size, square_size))

                # Add numbers on the left side
                if col == 0:
                    fonts = font.Font(None, 36)
                    number_text = fonts.render(str(8 - row), True, (0, 0, 0))
                    chess_board.blit(number_text, (x + 10, y + 5))

                # Add letters at the bottom
                if row == 7:
                    fonts = font.Font(None, 36)
                    letter_text = fonts.render(letters[col], True, (0, 0, 0))
                    chess_board.blit(letter_text, (x + square_size - 30, y + square_size - 30))

                # Set is_occupied for this tile
                is_occupied[row][col] = False  # Initially, no piece is present

        # Return the chess board surface and is_occupied
        return chess_board, is_occupied

    def get_tile_from_mouse_pos(self):

        mouse_x, mouse_y = mouse.get_pos()

        col = mouse_x // size
        row = mouse_y // size

        return row, col
