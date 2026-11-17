import pygame

from board import Board
from board_view import BoardView


def main():
    pygame.init()

    board = Board(width=20, height=14, cell_size=32)

    view = BoardView(board, offset=(20, 20))
    screen = pygame.display.set_mode((
        view.pixel_size[0] + 40,
        view.pixel_size[1] + 40,
    ))
    pygame.display.set_caption("Snake - Board demo")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((15, 15, 18))
        view.draw(screen)

        message = font.render(
            "ESC: quit",
            True, (235, 235, 235)
        )
        screen.blit(message, (20, view.pixel_size[1] + 27))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
