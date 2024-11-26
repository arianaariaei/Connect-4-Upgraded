from board import place_token, check_winner, is_board_full, get_valid_columns, evaluate_board
import time


def minimax(board, depth, maximizing_player, robot_player, node_counter):
    node_counter[0] += 1

    valid_columns = get_valid_columns(board)
    is_terminal = check_winner(board, 1) or check_winner(board, 2) or check_winner(board, 3) or is_board_full(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if check_winner(board, robot_player):
                return None, 100000  # Winning score for robot
            elif check_winner(board, 1) or check_winner(board, 2):
                return None, -100000  # Losing score
            else:
                return None, 0  # Draw
        else:
            return None, evaluate_board(board, robot_player)

    if maximizing_player:
        value = -float('inf')
        best_col = valid_columns[0]
        for col in valid_columns:
            temp_board = board.copy()
            place_token(temp_board, col, robot_player)
            _, new_score = minimax(temp_board, depth - 1, False, robot_player, node_counter)
            if new_score > value:
                value = new_score
                best_col = col
        return best_col, value
    else:
        value = float('inf')
        best_col = valid_columns[0]
        for col in valid_columns:
            temp_board = board.copy()
            for opponent in [1, 2]:
                temp_board_copy = temp_board.copy()
                place_token(temp_board_copy, col, opponent)
                _, new_score = minimax(temp_board_copy, depth - 1, True, robot_player, node_counter)
                if new_score < value:
                    value = new_score
                    best_col = col
        return best_col, value


def get_best_move(board, robot_player, depth=4):
    node_counter = [0]
    start_time = time.time()
    best_col, _ = minimax(board, depth, True, robot_player, node_counter)
    elapsed_time = time.time() - start_time

    print(f"Minimax: Explored {node_counter[0]} nodes in {elapsed_time:.4f} seconds.")
    return best_col
