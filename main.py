from menu import get_ai_algorithm_choice
from board import create_board, is_column_full, check_winner, is_board_full, place_token
import pygame
from runner import draw_board, handle_player_input, handle_robot_move, draw_message, init_pygame


def main():
    pygame.init()
    ai_algorithm = get_ai_algorithm_choice()
    if ai_algorithm is None:
        pygame.quit()
        return
    board = create_board()
    screen = init_pygame()

    current_player = 1
    robot_player = 3

    game_over = False

    while not game_over:
        draw_board(screen, board)

        if current_player != robot_player:
            col = None
            while col is None and not game_over:
                col = handle_player_input(screen, board, current_player)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                        break
                pygame.time.wait(50)

            if game_over:
                break

            if col is not None and not is_column_full(board, col):
                place_token(board, col, current_player)
        else:
            print("Robot is thinking...")
            col = handle_robot_move(board, robot_player, ai_algorithm)
            print(f"Robot chooses column {col}")
            place_token(board, col, robot_player)

        if check_winner(board, current_player):
            draw_board(screen, board)
            if current_player == robot_player:
                draw_message(screen, "Robot wins!", robot_player)
            else:
                draw_message(screen, f"Player {current_player} wins!",current_player)
            game_over = True
            pygame.time.wait(3000)
            continue

        if is_board_full(board):
            draw_board(screen, board)
            draw_message(screen, "Draw!")
            game_over = True
            pygame.time.wait(3000)
            continue

        current_player = 1 if current_player == 3 else current_player + 1

    pygame.quit()


if __name__ == "__main__":
    main()
