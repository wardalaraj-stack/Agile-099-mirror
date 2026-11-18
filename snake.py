
class Snake:
    """Stores the snake's position, body, direction, and color."""

    def __init__(self, x, y):
        self.__head = (x, y)
        self.__body = []
        self.__direction = (1, 0)
        self.__color = (0, 255, 0)

    def get_head(self):
        return self.__head

    def get_body(self):
        # copy prevents modifying the snake body without a defined method for it
        return self.__body.copy()

    def set_head(self, x, y):
        self.__head = (x, y)

    def get_direction(self):
        return self.__direction

    def get_color(self):
        return self.__color

