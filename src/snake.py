from src.snake_speed import SnakeSpeed

class Snake:
    """Stores the snake's position, body, direction, and color."""

    def __init__(self, x, y):
        self.__head = [x, y]
        self.__body = []
        self.__direction = (1, 0)
        self.__color = (0, 255, 0)
        self.__snake_speed = 3

    def get_head(self):
        return self.__head

    def get_body(self):
        # copy prevents modifying the snake body without a defined method for it
        return self.__body.copy()

    def set_head(self, x, y):
        self.__head = [x, y]

    def get_direction(self):
        return self.__direction

    def get_color(self):
        return self.__color

    def set_direction(self, x, y):
        self.__direction = (x, y)

    def get_snake_speed(self):
        return self.__snake_speed

    snakeSpeed = SnakeSpeed()

    def snake_move(self, cells_per_sec):
        self.cells_per_sec = cells_per_sec
        if(self.snakeSpeed.update(self.cells_per_sec)):
            self.set_head(self.get_head()[0] + self.get_direction()[0], self.get_head()[1] + self.get_direction()[1])
