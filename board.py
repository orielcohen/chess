from pygame import *


def create_chess_board():
    """
    Function to create a chess board using Pygame.

    Returns:
    --------
    pygame.Surface:
        The surface object representing the chess board.

    Raises:
    -------
    None
    """

    # Define the size of the chess board
    board_size = (600, 600)

    # Create a surface object to represent the chess board
    chess_board = Surface(board_size)

    # Define the colors for the chess board
    green = (118, 150, 86)
    light_green = (238, 238, 210)

    # Define the size of each square on the chess board
    square_size = board_size[0] // 8

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

    # Return the chess board surface
    return chess_board


def check_if_piece_is_pressed(piece_list):
    mouse_x, mouse_y = mouse.get_pos()
    colliding_pieces = None

    for piece in piece_list:
        # Check if the mouse click is inside the rectangle represented by 'piece'
        if piece.collidepoint(mouse_x, mouse_y):
            colliding_pieces = piece
            return colliding_pieces

    return colliding_pieces
