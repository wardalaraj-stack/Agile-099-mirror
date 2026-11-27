from tests.setup import setup, run
from tests.test_snake import create_snake, draw_snake
from tests.test_movement import move_snake
from src.key_input import KeyInput
from src.collision import hits_border


def check_collision(board, snake):
    if hits_border(snake.get_head(), board):
        return True

    if snake.ouroboros():
        return True
    
    return False


def main():
    board, view, screen, clock = setup()

    snake = create_snake(board)
    key_input = KeyInput()
    
    # Initialises the snake with a longer body for testing ouroborous
    x, y = snake.get_head()
    snake_length = len(snake.get_body())
    body_length = 8

    for body_part in range(snake_length, snake_length + body_length):
        snake.set_body(body_part, x - body_part, y)
        snake.increase_food_eaten()

    def update():
        move_snake(snake, key_input)

        if check_collision(board, snake):
            return False

    def draw():
        draw_snake(screen, view, snake)

    run(view, screen, clock, draw, key_input.set_direction, update)


if __name__ == "__main__":
    main()
