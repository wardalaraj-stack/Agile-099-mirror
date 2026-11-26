import pygame

from src.key_input import KeyInput
from src.snake import Snake
from src.board import Board
from src.board_view import BoardView
from src.Food import Food
from src.Food_drawing import Food_drawing
from src.collision import random_position, find_free_spot

SNAKE_HEAD_INSET = 6


def draw_snake_head(surface, board_view, head_position, head_color):
    head_rect = board_view.cell_rect(head_position).inflate(
        -2 * SNAKE_HEAD_INSET,
        -2 * SNAKE_HEAD_INSET
    )
    pygame.draw.ellipse(surface, head_color, head_rect)


def main():
    pygame.init()

    board = Board(width=40, height=20, cell_size=32)

    board_view = BoardView(board, offset=(20, 20))
    screen = pygame.display.set_mode((
        board_view.pixel_size[0] + 40,
        board_view.pixel_size[1] + 40,
    ))
    pygame.display.set_caption("Snake - Board demo")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)

    key_input = KeyInput()
    randomspot = random_position(board)
    snake = Snake(randomspot[0], randomspot[1])
    
    #Food Logic
    freeSpot = find_free_spot(board, snake.get_head(), snake.get_body())
    food = Food(freeSpot[0], freeSpot[1])
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            key_input.set_direction(event)
        snake.set_direction(*key_input.get_direction())

        screen.fill((15, 15, 18))
        board_view.draw(screen)

        # Render the snake's head
        draw_snake_head(screen, board_view, snake.get_head(), snake.get_color())

        quit_message = font.render(
            "ESC: quit",
            True, (235, 235, 235)
        )
        screen.blit(quit_message, (20, board_view.pixel_size[1] + 27))

        pygame.display.flip()
        clock.tick(60)

        # Speed of snake
        snake.move(snake.get_speed())

        #Food spawining Logic
        Food_drawing.Draw_food(screen, board_view, food)


    pygame.quit()


if __name__ == "__main__":
    main()
