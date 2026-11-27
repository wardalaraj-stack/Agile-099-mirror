import pygame

from src.board import Board
from src.board_view import BoardView

def setup():
    pygame.init()

    board = Board()
    view = BoardView(board)
    screen = pygame.display.set_mode(view.pixel_size)
    clock = pygame.time.Clock()

    return board, view, screen, clock


def run(
    view, 
    screen, 
    clock, 
    draw=None,
    handle_event=None,
    update=None
):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            if handle_event is not None:
                handle_event(event)

        if update is not None:
            if update() is False:
                running = False

        view.draw(screen)

        if draw is not None:
            draw()

        pygame.display.flip()
        
        # Refresh rate
        clock.tick(60)

    pygame.quit()
