from board import *
from pieces import *

# Board positions
positions = [(col, row) for col in range(8) for row in range(8)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

# initialize pygame
init()

# create the screen
screen = display.set_mode((600, 600))

# title and icon
display.set_caption('Chess')
icon = image.load('Images/b_pawn.png')
display.set_icon(icon)

# piece images
bp_image = image.load('Images/b_pawn.png')
wp_image = image.load('Images/w_pawn.png')
bk_image = image.load('Images/b_king.png')
wk_image = image.load('Images/w_king.png')
br_image = image.load('Images/b_rook.png')
wr_image = image.load('Images/w_rook.png')
bb_image = image.load('Images/b_bishop.png')
wb_image = image.load('Images/w_bishop.png')
bq_image = image.load('Images/b_queen.png')
wq_image = image.load('Images/w_queen.png')
bkn_image = image.load('Images/b_knight.png')
wkn_image = image.load('Images/w_knight.png')

# Initialize the game and chess board
game = Game()
board = game.board
is_occupied = game.is_occupied
# Size of squares
size = 75

# board length, must be even
screen.fill(WHITE)
screen.blit(board, (0, 0))

# Create pieces
white_pieces = [
    Rook(wr_image, (c_a, r_1), "white"),
    Knight(wkn_image, (c_b, r_1), "white"),
    Bishop(wb_image, (c_c, r_1), "white"),
    Queen(wq_image, (c_d, r_1), "white"),
    King(wk_image, (c_e, r_1), "white"),
    Bishop(wb_image, (c_f, r_1), "white"),
    Knight(wkn_image, (c_g, r_1), "white"),
    Rook(wr_image, (c_h, r_1), "white"),
    Pawn(wp_image, (c_a, r_2), "white"),
    Pawn(wp_image, (c_b, r_2), "white"),
    Pawn(wp_image, (c_c, r_2), "white"),
    Pawn(wp_image, (c_d, r_2), "white"),
    Pawn(wp_image, (c_e, r_2), "white"),
    Pawn(wp_image, (c_f, r_2), "white"),
    Pawn(wp_image, (c_g, r_2), "white"),
    Pawn(wp_image, (c_h, r_2), "white")
]

black_pieces = [
    Rook(br_image, (c_a, r_8), "black"),
    Knight(bkn_image, (c_b, r_8), "black"),
    Bishop(bb_image, (c_c, r_8), "black"),
    Queen(bq_image, (c_d, r_8), "black"),
    King(bk_image, (c_e, r_8), "black"),
    Bishop(bb_image, (c_f, r_8), "black"),
    Knight(bkn_image, (c_g, r_8), "black"),
    Rook(br_image, (c_h, r_8), "black"),
    Pawn(bp_image, (c_a, r_7), "black"),
    Pawn(bp_image, (c_b, r_7), "black"),
    Pawn(bp_image, (c_c, r_7), "black"),
    Pawn(bp_image, (c_d, r_7), "black"),
    Pawn(bp_image, (c_e, r_7), "black"),
    Pawn(bp_image, (c_f, r_7), "black"),
    Pawn(bp_image, (c_g, r_7), "black"),
    Pawn(bp_image, (c_h, r_7), "black")
]

all_pieces = white_pieces + black_pieces

for piece in all_pieces:
    row, col = piece.get_current_position()
    is_occupied[row][col] = piece


running = True
selected_piece = None
tile_clicked = None  # Initialize tile_clicked outside the loop

while running:
    for events in event.get():
        if events.type == QUIT:
            running = False

        if events.type == MOUSEBUTTONDOWN:
            if selected_piece is None:
                for piece in all_pieces:
                    if piece.check_if_piece_is_pressed():
                        selected_piece = piece
                        break
            else:
                tile_clicked = game.get_tile_from_mouse_pos()
                if tile_clicked is not None:
                    row, col = tile_clicked
                    valid_moves = selected_piece.check_valid_moves(is_occupied)
                    if (row, col) in valid_moves:
                        # Check if there's a piece on the target tile
                        target_piece = is_occupied[row][col]
                        if target_piece is not None:
                            all_pieces.remove(target_piece)  # Remove the taken piece
                        # Perform the move
                        selected_piece_x, selected_piece_y = selected_piece.get_current_position()
                        is_occupied[selected_piece_x][selected_piece_y] = None
                        selected_piece.move(tile_clicked, valid_moves)
                        is_occupied[row][col] = selected_piece

                    selected_piece = None

    screen.fill(WHITE)
    screen.blit(board, (0, 0))

    for piece in all_pieces:
        piece.redraw()

    display.flip()
