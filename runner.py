import pygame

SQUARE_SIZE = 60
PURPLE1 = (193, 179, 215)
PURPLE2 = (221, 212, 232)
BLUE = (154, 206, 223)
YELLOW = (255, 250, 129)
GREEN = (181, 225, 174)


def draw_board(screen, board):
    """
    Draws the game board using Pygame.
    """
    for row in range(10):
        for col in range(10):
            # Draw the blue rectangle for each cell
            pygame.draw.rect(screen, PURPLE1, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            # Draw the circle in each cell
            pygame.draw.circle(screen, PURPLE2,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                               SQUARE_SIZE // 2 - 5)

            # Draw the player tokens
            if board[row][col] == 1:  # Player 1
                pygame.draw.circle(screen, BLUE,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)
            elif board[row][col] == 2:  # Player 2
                pygame.draw.circle(screen, YELLOW,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)
            elif board[row][col] == 3:  # Robot
                pygame.draw.circle(screen, GREEN,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)

    pygame.display.update()


def handle_player_input(screen, board, player):
    """
    Handles human player input using Pygame events.
    Returns the selected column or None if no selection was made.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the x position of the mouse click
            posx = event.pos[0]
            # Convert the x position to a column number (0-9)
            col = posx // SQUARE_SIZE

            if 0 <= col < 10:  # Ensure valid column
                return col

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()

    return None


def handle_robot_move(board, robot_player, ai_algorithm):
    """
    Handles the robot's move using the selected AI algorithm.
    Returns the selected column.
    """
    from minimax import get_best_move
    from alpha_beta import get_best_move_alpha_beta

    if ai_algorithm == "minimax":
        return get_best_move(board, robot_player)
    else:
        return get_best_move_alpha_beta(board, robot_player)


def draw_message(screen, message, winner):
    """
    Displays a message on the screen.
    """
    font = pygame.font.Font(None, 74)
    if winner == 1:
        text = font.render(message, True, BLUE)
    elif winner == 2:
        text = font.render(message, True, YELLOW)
    elif winner == 3:
        text = font.render(message, True, GREEN)

    text_rect = text.get_rect(center=(5 * SQUARE_SIZE, 5 * SQUARE_SIZE))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)


def init_pygame():
    """
    Initializes Pygame and creates the game window.
    """
    pygame.init()
    screen = pygame.display.set_mode((10 * SQUARE_SIZE, 10 * SQUARE_SIZE))
    pygame.display.set_caption('Connect 4 - Three Players')
    return screen