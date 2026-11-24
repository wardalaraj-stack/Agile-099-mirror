import pygame
from Key_input import KeyInput
from snake import Snake
from board import Board
from board_view import BoardView

#### test marker for borders#####
MARKER_COLOR = (36, 91, 149)
MARKER_INSET = 6
DIRECTIONS = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
}


def next_marker_position(board, position, step):
    column, row = position
    column_step, row_step = step
    candidate = column + column_step, row + row_step
    return position if board.outside_edges(candidate) else candidate


def draw_marker(surface, view, position):
    rect = view.cell_rect(position).inflate(-2 * MARKER_INSET, -2 * MARKER_INSET)
    pygame.draw.ellipse(surface, MARKER_COLOR, rect)
#### end test marker for bordar

def main():
    pygame.init()

    board = Board(width=40, height=20, cell_size=32)

    view = BoardView(board, offset=(20, 20))
    screen = pygame.display.set_mode((
        view.pixel_size[0] + 40,
        view.pixel_size[1] + 40,
    ))
    pygame.display.set_caption("Snake - Board demo")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)
    key_input = KeyInput()
    snake = Snake(0, 0)



    position = (0, 0)               # possition of test marker
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    ##checks whether the pressed key is an arrow key. If it is,
                    ##the code moves the marker one cell in that direction and saves its new position. 
                    ## The helper(next marker possitionn) keeps it from moving off the board.
            key_input.set_direction(event)
        snake.set_direction(*key_input.get_direction())
        #print(snake.get_direction())
        #print(snake.get_head())
        
        screen.fill((15, 15, 18))
        view.draw(screen)
        draw_marker(screen, view, position)         #draw for test marker 

        message = font.render(
            "ESC: quit",
            True, (235, 235, 235)
        )
        screen.blit(message, (20, view.pixel_size[1] + 27))

        pygame.display.flip()
        clock.tick(60)
        
        if snake.snake_move(snake.get_snake_speed()) is False:
        # returns False when the next move collides with the snake’s body
            running = False
        position = snake.get_head()

    pygame.quit()


    


if __name__ == "__main__":
    main()
