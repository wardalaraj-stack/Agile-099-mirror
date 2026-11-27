from tests.setup import setup, run
from tests.test_snake import create_snake, draw_snake
from tests.test_movement import move_snake
from src.key_input import KeyInput
from src.Food import Food
from src.Food_drawing import Food_drawing
from src.collision import find_free_spot, food_collision


def create_food(board, snake):
    x, y = find_free_spot(board, snake.get_head(), snake.get_body())

    return Food(x, y)


def draw_food(screen, view, food):
    Food_drawing.Draw_food(screen, view, food)


def update_food(board, snake, food):
    if food_collision(food.getFood(), snake.get_head()):
        snake.increase_food_eaten()

        x, y = find_free_spot(board, snake.get_head(), snake.get_body())

        food.newFood(x, y)


def main():
    board, view, screen, clock = setup()

    snake = create_snake(board)
    food = create_food(board, snake)
    key_input = KeyInput()

    def update():
        move_snake(snake, key_input)
        update_food(board, snake, food)

    def draw():
        draw_snake(screen, view, snake)
        draw_food(screen, view, food)

    run(view, screen, clock, draw, key_input.set_direction, update)


if __name__ == "__main__":
    main()
