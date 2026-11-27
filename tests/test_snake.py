from tests.setup import setup, run
from src.snake import Snake
# This should probably be moved from board_launch
from src.board_launch import draw_snake_head, draw_body


def create_snake(board):
    x = board.width // 2
    y = board.height // 2

    return Snake(x, y)


def draw_snake(screen, view, snake):
    for position in snake.get_body():
        draw_body(screen, view, position)

    draw_snake_head(screen, view, snake.get_head(), snake.get_color())


def main():
    board, view, screen, clock = setup()
    snake = create_snake(board)

    def draw():
        draw_snake(screen, view, snake)

    run(view, screen, clock, draw)


if __name__ == "__main__":
    main()
