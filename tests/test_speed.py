from tests.setup import setup, run
from tests.test_snake import create_snake, draw_snake
from tests.test_movement import move_snake
from src.key_input import KeyInput


def main():
    board, view, screen, clock = setup()

    snake = create_snake(board)
    key_input = KeyInput()

    # I'm not sure whether changing the speed works or not.
    # We should probably investigate the implementation.

    # Change the speed of the snake here
    speed = 8

    def update():
        move_snake(snake, key_input, speed)

    def draw():
        draw_snake(screen, view, snake)

    run(view, screen, clock, draw, key_input.set_direction, update)


if __name__ == "__main__":
    main()
