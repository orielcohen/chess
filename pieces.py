from pygame import *

# Initialize pygame
init()

# Set up the screen
screen = display.set_mode((600, 600))
size = 75

# Board positions
positions = [(col, row) for col in range(8) for row in range(8)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



class Piece(sprite.Sprite):
    def __init__(self, img, position, colour):
        super().__init__()
        self.img = img
        self.image = img
        self.colour = colour
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def check_if_piece_is_pressed(self):
        mouse_x, mouse_y = mouse.get_pos()
        return self.rect.collidepoint(mouse_x, mouse_y)

    def redraw(self):
        screen.blit(self.image, self.rect.topleft)

    def get_current_position(self):
        col = self.rect.topleft[0] // size
        row = self.rect.topleft[1] // size
        return row, col

    def move(self, location_pressed, valid_moves):
        if location_pressed in valid_moves:
            x = location_pressed[1] * size
            y = location_pressed[0] * size
            self.rect.topleft = (x, y)
            # Additional logic for pawn promotion (if needed)
            if isinstance(self, Pawn):
                row, _ = location_pressed
                if row == 0 or row == 7:
                    # Handle pawn promotion here (e.g., replace with a queen)
                    pass


class Pawn(Piece):
    def __init__(self, img, position, colour):
        super().__init__(img, position, colour)

    def check_valid_moves(self, is_occupied):
        valid_moves = []
        row, col = self.get_current_position()
        direction = -1 if self.colour == "white" else 1

        # Move forward
        if 0 <= row + direction < 8 and is_occupied[row + direction][col] is None:
            valid_moves.append((row + direction, col))

        # Initial double move
        if (
                (self.colour == "white" and row == 6) or
                (self.colour == "black" and row == 1)
        ) and is_occupied[row + direction][col] is None and is_occupied[row + 2 * direction][col] is None:
            valid_moves.append((row + 2 * direction, col))

        # Captures
        if 0 <= row + direction < 8 and 0 <= col - 1 < 8:
            target = is_occupied[row + direction][col - 1]
            if target is not None and target.colour != self.colour:
                valid_moves.append((row + direction, col - 1))
        if 0 <= row + direction < 8 and 0 <= col + 1 < 8:
            target = is_occupied[row + direction][col + 1]
            if target is not None and target.colour != self.colour:
                valid_moves.append((row + direction, col + 1))

        return valid_moves


class Rook(Piece):
    def __init__(self, img, position, colour):
        super().__init__(img, position, colour)

    def check_valid_moves(self, is_occupied):
        valid_moves = []
        row, col = self.get_current_position()

        for i in range(row - 1, -1, -1):
            target = is_occupied[i][col]
            if target is None:
                valid_moves.append((i, col))
            else:
                if target.colour != self.colour:
                    valid_moves.append((i, col))
                break

        for i in range(row + 1, 8):
            target = is_occupied[i][col]
            if target is None:
                valid_moves.append((i, col))
            else:
                if target.colour != self.colour:
                    valid_moves.append((i, col))
                break

        for i in range(col - 1, -1, -1):
            target = is_occupied[row][i]
            if target is None:
                valid_moves.append((row, i))
            else:
                if target.colour != self.colour:
                    valid_moves.append((row, i))
                break

        for i in range(col + 1, 8):
            target = is_occupied[row][i]
            if target is None:
                valid_moves.append((row, i))
            else:
                if target.colour != self.colour:
                    valid_moves.append((row, i))
                break

        return valid_moves


class Knight(Piece):
    def __init__(self, img, position, colour):
        super().__init__(img, position, colour)

    def check_valid_moves(self, is_occupied):
        valid_moves = []
        row, col = self.get_current_position()
        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target = is_occupied[new_row][new_col]
                if target is None or target.colour != self.colour:
                    valid_moves.append((new_row, new_col))
        return valid_moves


class Bishop(Piece):
    def __init__(self, img, position, colour):
        super().__init__(img, position, colour)

    def check_valid_moves(self, is_occupied):
        valid_moves = []
        row, col = self.get_current_position()
        for i in range(1, 8):
            if row - i >= 0 and col - i >= 0:
                target = is_occupied[row - i][col - i]
                if target is None:
                    valid_moves.append((row - i, col - i))
                else:
                    if target.colour != self.colour:
                        valid_moves.append((row - i, col - i))
                    break
            else:
                break

        for i in range(1, 8):
            if row - i >= 0 and col + i < 8:
                target = is_occupied[row - i][col + i]
                if target is None:
                    valid_moves.append((row - i, col + i))
                else:
                    if target.colour != self.colour:
                        valid_moves.append((row - i, col + i))
                    break
            else:
                break

        for i in range(1, 8):
            if row + i < 8 and col - i >= 0:
                target = is_occupied[row + i][col - i]
                if target is None:
                    valid_moves.append((row + i, col - i))
                else:
                    if target.colour != self.colour:
                        valid_moves.append((row + i, col - i))
                    break
            else:
                break

        for i in range(1, 8):
            if row + i < 8 and col + i < 8:
                target = is_occupied[row + i][col + i]
                if target is None:
                    valid_moves.append((row + i, col + i))
                else:
                    if target.colour != self.colour:
                        valid_moves.append((row + i, col + i))
                    break
            else:
                break
        return valid_moves


class Queen(Piece):

    def __init__(self, img, position, colour):
        super().__init__(img, position, colour)

    def check_valid_moves(self, is_occupied):
        valid_moves = []
        row, col = self.get_current_position()
        # Diagonal moves
        for i in range(1, 8):
            if row - i >= 0 and col - i >= 0:
                target = is_occupied[row - i][col - i]
                if target is None:
                    valid_moves.append((row - i, col - i))
                else:
                    if target.colour != self.colour:
                        valid_moves.append((row - i, col - i))
                    break
            else:
                break

        for i in range(1, 8):
            if row - i >= 0 and col + i < 8:
                target = is_occupied[row - i][col + i]
                if target is None:
                    valid_moves.append((row - i, col + i))
                else:
                    if target.colour != self.colour:
                        valid_moves.append((row - i, col + i))
                    break
            else:
                break

        for i in range(1, 8):
            if row + i < 8 and col - i >= 0:
                target = is_occupied[row + i][col - i]
                if target is None:
                    valid_moves.append((row + i, col - i))
                else:
                    if target.colour != self.colour:
                        valid_moves.append((row + i, col - i))
                    break
            else:
                break

        for i in range(1, 8):
            if row + i < 8 and col + i < 8:
                target = is_occupied[row + i][col + i]
                if target is None:
                    valid_moves.append((row + i, col + i))
                else:
                    if target.colour != self.colour:
                        valid_moves.append((row + i, col + i))
                    break
            else:
                break

        # Vertical moves
        for i in range(row - 1, -1, -1):
            target = is_occupied[i][col]
            if target is None:
                valid_moves.append((i, col))
            else:
                if target.colour != self.colour:
                    valid_moves.append((i, col))
                break

        for i in range(row + 1, 8):
            target = is_occupied[i][col]
            if target is None:
                valid_moves.append((i, col))
            else:
                if target.colour != self.colour:
                    valid_moves.append((i, col))
                break

        # Horizontal moves
        for i in range(col - 1, -1, -1):
            target = is_occupied[row][i]
            if target is None:
                valid_moves.append((row, i))
            else:
                if target.colour != self.colour:
                    valid_moves.append((row, i))
                break

        for i in range(col + 1, 8):
            target = is_occupied[row][i]
            if target is None:
                valid_moves.append((row, i))
            else:
                if target.colour != self.colour:
                    valid_moves.append((row, i))
                break

        return valid_moves


class King(Piece):
    def __init__(self, img, position, colour):
        super().__init__(img, position, colour)

    def check_valid_moves(self, is_occupied):
        valid_moves = []
        row, col = self.get_current_position()
        moves = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target = is_occupied[new_row][new_col]
                if target is None or target.colour != self.colour:
                    valid_moves.append((new_row, new_col))
        return valid_moves
