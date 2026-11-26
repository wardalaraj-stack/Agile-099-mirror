from src.snake_speed import SnakeSpeed


class Snake:
    """Stores the snake's position, body, direction, and color."""

    def __init__(self, x, y):
        self.__head = [x, y]
        self.__body = []
        self.__direction = (1, 0)
        self.__color = (0, 255, 0)
        self.__speed = 3

    def get_head(self):
        return self.__head

    def get_body(self):
        # Prevents direct modification of the snake's body.
        return self.__body.copy()

    def set_head(self, x, y):
        self.__head = [x, y]

    def get_direction(self):
        return self.__direction

    def get_color(self):
        return self.__color

    def set_direction(self, x, y):
        self.__direction = (x, y)

    def get_speed(self):
        return self.__speed

    speed_controller = SnakeSpeed()

    def move(self, cells_per_sec):
        self.cells_per_sec = cells_per_sec
        if self.speed_controller.update(self.cells_per_sec):
            self.set_head(
                self.get_head()[0] + self.get_direction()[0],
                self.get_head()[1] + self.get_direction()[1]
            )
