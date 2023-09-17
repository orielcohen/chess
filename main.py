from board import *
from pieces import *

WHITE = (255, 255, 255)

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
a1, a2, a3, a4, a5, a6, a7, a8 = (c_a, r_1), (c_a, r_2), (c_a, r_3), (c_a, r_4), (c_a, r_5), (c_a, r_6), (c_a, r_7), \
                                 (c_a, r_8)

b1, b2, b3, b4, b5, b6, b7, b8 = (c_b, r_1), (c_b, r_2), (c_b, r_3), (c_b, r_4), (c_b, r_5), (c_b, r_6), (c_b, r_7), \
                                 (c_b, r_8)

c1, c2, c3, c4, c5, c6, c7, c8 = (c_c, r_1), (c_c, r_2), (c_c, r_3), (c_c, r_4), (c_c, r_5), (c_c, r_6), (c_c, r_7), \
                                 (c_c, r_8)

d1, d2, d3, d4, d5, d6, d7, d8 = (c_d, r_1), (c_d, r_2), (c_d, r_3), (c_d, r_4), (c_d, r_5), (c_d, r_6), (c_d, r_7), \
                                 (c_d, r_8)

e1, e2, e3, e4, e5, e6, e7, e8 = (c_e, r_1), (c_e, r_2), (c_e, r_3), (c_e, r_4), (c_e, r_5), (c_e, r_6), (c_e, r_7), \
                                 (c_e, r_8)

f1, f2, f3, f4, f5, f6, f7, f8 = (c_f, r_1), (c_f, r_2), (c_f, r_3), (c_f, r_4), (c_f, r_5), (c_f, r_6), (c_f, r_7), \
                                 (c_f, r_8)

g1, g2, g3, g4, g5, g6, g7, g8 = (c_g, r_1), (c_g, r_2), (c_g, r_3), (c_g, r_4), (c_g, r_5), (c_g, r_6), (c_g, r_7), \
                                 (c_g, r_8)

h1, h2, h3, h4, h5, h6, h7, h8 = (c_h, r_1), (c_h, r_2), (c_h, r_3), (c_h, r_4), (c_h, r_5), (c_h, r_6), (c_h, r_7), \
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

# Create the chess board
board = create_chess_board()
# Size of squares
size = 75

# board length, must be even
screen.fill(WHITE)
screen.blit(board, (0, 0))

# white pieces setup
wr_a1 = Rook(wr_image, a1)
wkn_b1 = Knight(wkn_image, b1)
wb_c1 = Bishop(wb_image, c1)
wq = Queen(wq_image, d1)
wk = King(wk_image, e1)
wb_f1 = Bishop(wb_image, f1)
wkn_g1 = Knight(wkn_image, g1)
wr_h1 = Rook(wr_image, h1)

wp_a2 = Pawn(wp_image, a2)
wp_b2 = Pawn(wp_image, b2)
wp_c2 = Pawn(wp_image, c2)
wp_d2 = Pawn(wp_image, d2)
wp_e2 = Pawn(wp_image, e2)
wp_f2 = Pawn(wp_image, f2)
wp_g2 = Pawn(wp_image, g2)
wp_h2 = Pawn(wp_image, h2)

# black pieces setup
br_a8 = Rook(br_image, a8)
bkn_b8 = Knight(bkn_image, b8)
bb_c8 = Bishop(bb_image, c8)
bq = Queen(bq_image, d8)
bk = King(bk_image, e8)
bb_f8 = Bishop(bb_image, f8)
bkn_g8 = Knight(bkn_image, g8)
br_h8 = Rook(br_image, h8)

bp_a7 = Pawn(bp_image, a7)
bp_b7 = Pawn(bp_image, b7)
bp_c7 = Pawn(bp_image, c7)
bp_d7 = Pawn(bp_image, d7)
bp_e7 = Pawn(bp_image, e7)
bp_f7 = Pawn(bp_image, f7)
bp_g7 = Pawn(bp_image, g7)
bp_h7 = Pawn(bp_image, h7)

pieces_list = [wr_a1, wkn_b1, wb_c1, wq, wk, wb_f1, wkn_g1, wr_h1, wp_a2, wp_b2, wp_c2, wp_d2, wp_e2, wp_f2, wp_g2,
               wp_h2,
               br_a8, bkn_b8, bb_c8, bq, bk, bb_f8, bkn_g8, br_h8, bp_a7, bp_b7, bp_c7, bp_d7, bp_e7, bp_f7, bp_g7,
               bp_h7]

running = True
selected_piece = None  # Variable to store the selected piece

# game loop
while running:
    for events in event.get():
        if events.type == QUIT:
            running = False

        if events.type == MOUSEBUTTONDOWN:
            selected_piece = check_if_piece_is_pressed(pieces_list)
            if selected_piece is not None:
                selected_piece.move((0, 75))
                print(selected_piece)
                display.flip()

    display.flip()
