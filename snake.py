from snake_speed import SnakeSpeed

class Snake:
    """Stores the snake's position, body, direction, and color."""

    def __init__(self, x, y):
        self.__head = [x, y]
        self.__body = [x, y]
        self.__direction = (1, 0)
        self.__color = (0, 255, 0)
        self.__snake_speed = 3
        self.__foodEaten = 2
        self.spawnBody()

    def spawnBody(self):
        self.set_body(1, self.get_head().x - self.get_direction().x, self.get_head().y - self.get_direction().y)
        self.set_body(2, self.get_head().x - ( 2 *self.get_direction().x), self.get_head().y - ( 2 * self.get_direction().y))
        

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

    def set_body(self, index, x, y):
        if (index => len(self.get_body())):
            self.__body.append([x,y])
        else:
            self.__body[index].x = x
            self.__body[index].y = y

    def removeLastTail(self):
        return self.__body.remove(len(self.get_body()-1))
    

    def get_snake_speed(self):
        return self.__snake_speed

    def get_food_eaten(self):
        return self.__foodEaten

    snakeSpeed = SnakeSpeed()

    def snakeUpdate(self, cells_per_sec):
        self.cells_per_sec = cells_per_sec
        if(self.snakeSpeed.update(self.cells_per_sec)):
            self.snake_move()
            self.snakeBodyMovement()

    def snake_move(self):                
        self.set_head(self.get_head()[0] + self.get_direction()[0], self.get_head()[1] + self.get_direction()[1])

    def snakeBodyMovement(self):
        for i in (range(self.get_food_eaten, 0, -1)):
            if not(i == 0):
                self.set_body(i, self.get_body()[i-1].x, self.get_body()[i-1].y)
                continue

            self.set_body(i, self.get_head().x, self.get_head().y)
            if(len(self.get_body) > self.get_food_eaten):
                self.removeLastTail()
