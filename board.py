import numpy as np


def create_board():
    return np.zeros((10, 10), dtype=int)


def is_column_full(board, col):
    return board[0, col] != 0


def is_board_full(board):
    return not np.any(board == 0)


def place_token(board, col, player):
    for row in range(9, -1, -1):
        if board[row, col] == 0:
            board[row, col] = player
            return True
    return False


def check_winner(board, player):
    rows, cols = board.shape

    for row in range(rows):
        for col in range(cols - 3):
            if all(board[row, col + i] == player for i in range(4)):
                return True

    for col in range(cols):
        for row in range(rows - 3):
            if all(board[row + i, col] == player for i in range(4)):
                return True

    for row in range(rows - 3):
        for col in range(cols - 3):
            if all(board[row + i, col + i] == player for i in range(4)):
                return True

    for row in range(rows - 3):
        for col in range(3, cols):
            if all(board[row + i, col - i] == player for i in range(4)):
                return True

    return False


def evaluate_window(window, player):
    """
    Evaluates a 4-cell window for scoring purposes.
    Assigns positive scores for the robot's tokens and negative scores for opponents.
    """
    score = 0
    opponent = 1 if player == 3 else 3

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(0) == 1:
        score += 10
    elif window.count(player) == 2 and window.count(0) == 2:
        score += 5

    if window.count(opponent) == 3 and window.count(0) == 1:
        score -= 8

    return score


def evaluate_board(board, player):
    """
    Evaluates the current state of the board and returns a score.
    """
    score = 0

    for row in range(10):
        for col in range(7):
            window = board[row, col:col + 4].tolist()
            score += evaluate_window(window, player)

    for col in range(10):
        for row in range(7):
            window = board[row:row + 4, col].tolist()
            score += evaluate_window(window, player)

    for row in range(7):
        for col in range(7):
            window = [board[row + i, col + i] for i in range(4)]
            score += evaluate_window(window, player)

    for row in range(7):
        for col in range(3, 10):
            window = [board[row + i, col - i] for i in range(4)]
            score += evaluate_window(window, player)

    return score


def get_valid_columns(board):
    return [col for col in range(10) if not is_column_full(board, col)]
