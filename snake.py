from collision import snake_hits_itself
from snake_speed import SnakeSpeed


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


    def snake_move(self, cells_per_sec, growing=False):
        #modified for snake collision with self(for now)/others(for futture)
        self.cells_per_sec = cells_per_sec
        if not self.snakeSpeed.update(self.cells_per_sec):
            return None

        head = self.get_head()
        direction = self.get_direction()
        next_head = [head[0] + direction[0], head[1] + direction[1]]

        if snake_hits_itself(next_head, self.__body, growing):
            return False

        self.__body.insert(0, head.copy())
        if not growing:
            self.__body.pop()
        self.set_head(*next_head)
        return True
    # end of collition modification
