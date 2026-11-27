from tests.setup import setup, run
from tests.test_snake import create_snake, draw_snake
from src.key_input import KeyInput


def move_snake(snake, key_input, speed=None):
    if speed is None:
        speed = snake.get_snake_speed()

    snake.set_direction(*key_input.get_direction())
    snake.snakeUpdate(snake.get_snake_speed())


def main():
    board, view, screen, clock = setup()

    snake = create_snake(board)
    key_input = KeyInput()

    def update():
        move_snake(snake, key_input)

    def draw():
        draw_snake(screen, view, snake)

    run(view, screen, clock, draw, key_input.set_direction, update)


if __name__ == "__main__":
    main()
