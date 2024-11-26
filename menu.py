import pygame


class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (59, 130, 246)
    LIGHT_BLUE = (219, 234, 254)
    GRAY = (75, 85, 99)
    PURPLE1 = (193, 179, 215)
    PURPLE2 = (221, 212, 232)


class Button:
    def __init__(self, x, y, width, height, text, subtitle):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.subtitle = subtitle
        self.hovered = False
        self.clicked = False

    def draw(self, screen, font_large, font_small):
        # Draw button background with shadow
        shadow_rect = self.rect.copy()
        shadow_rect.y += 4
        pygame.draw.rect(screen, Colors.PURPLE1, shadow_rect, border_radius=12)

        # Draw main button
        color = Colors.PURPLE2 if self.hovered else Colors.WHITE
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        if self.hovered:
            pygame.draw.rect(screen, Colors.PURPLE1, self.rect, 2, border_radius=12)

        # Draw main text
        text_surface = font_large.render(self.text, True, Colors.BLACK)
        text_rect = text_surface.get_rect(
            topleft=(self.rect.x + 20, self.rect.y + 15)
        )
        screen.blit(text_surface, text_rect)

        # Draw subtitle
        subtitle_surface = font_small.render(self.subtitle, True, Colors.GRAY)
        subtitle_rect = subtitle_surface.get_rect(
            topleft=(self.rect.x + 20, self.rect.y + 50)
        )
        screen.blit(subtitle_surface, subtitle_rect)

        # Draw arrow if hovered
        if self.hovered:
            arrow_points = [
                (self.rect.right - 40, self.rect.centery),
                (self.rect.right - 30, self.rect.centery - 5),
                (self.rect.right - 30, self.rect.centery + 5)
            ]
            pygame.draw.polygon(screen, Colors.PURPLE1, arrow_points)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                self.clicked = True
                return True
        return False


def get_ai_algorithm_choice():
    # Set up display
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connect 4 - AI Algorithm Selection")

    # Set up fonts
    font_large = pygame.font.Font(None, 36)
    font_small = pygame.font.Font(None, 24)
    font_title = pygame.font.Font(None, 64)

    # Create buttons
    button_width = 400
    button_height = 100
    button_x = (WIDTH - button_width) // 2

    minimax_button = Button(
        button_x, 200, button_width, button_height,
        "Minimax Algorithm",
        "Classic decision-making algorithm"
    )

    alpha_beta_button = Button(
        button_x, 320, button_width, button_height,
        "Alpha-Beta Pruning",
        "Enhanced version of Minimax"
    )

    running = True
    ai_algorithm = None

    while running:
        screen.fill(Colors.PURPLE1)

        # Draw gradient background
        for i in range(HEIGHT):
            progress = i / HEIGHT
            color = [
                int(219 + (234 - 219) * progress),
                int(234 + (246 - 234) * progress),
                int(254 + (255 - 254) * progress)
            ]
            pygame.draw.line(screen, color, (0, i), (WIDTH, i))

        # Draw title
        title_surface = font_title.render("Connect Four", True, Colors.BLACK)
        subtitle_surface = font_large.render("Select AI Algorithm", True, Colors.GRAY)

        title_rect = title_surface.get_rect(center=(WIDTH // 2, 80))
        subtitle_rect = subtitle_surface.get_rect(center=(WIDTH // 2, 130))

        screen.blit(title_surface, title_rect)
        screen.blit(subtitle_surface, subtitle_rect)

        # Draw buttons
        minimax_button.draw(screen, font_large, font_small)
        alpha_beta_button.draw(screen, font_large, font_small)

        # Draw footer
        footer_surface = font_small.render("Press ESC to quit the game", True, Colors.GRAY)
        footer_rect = footer_surface.get_rect(center=(WIDTH // 2, HEIGHT - 40))
        screen.blit(footer_surface, footer_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None

            if minimax_button.handle_event(event):
                ai_algorithm = "minimax"
                running = False

            if alpha_beta_button.handle_event(event):
                ai_algorithm = "alpha_beta"
                running = False

    return ai_algorithm
