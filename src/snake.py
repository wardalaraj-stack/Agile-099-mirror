from src.snake_speed import SnakeSpeed
from src.collision import snake_hits_itself


class Snake:
    """Stores the snake's position, body, direction, and color."""

    def __init__(self, x, y):
        self.__head = (x, y)
        self.__body = [(x, y)]
        self.__direction = (1, 0)
        self.__color = (0, 255, 0)
        self.__speed = 3
        self.__snake_speed = 6
        self.__startingBodyLenght = 3
        self.__foodEaten = 0
        self.spawnBody()

    def spawnBody(self):
        for i in range(self.get_starting_lenght() +1):
            self.set_body(i, self.get_head()[0] - ( i *self.get_direction()[0]), self.get_head()[1] - (i * self.get_direction()[1]))
        

    def get_head(self):
        return self.__head

    def get_body(self):
        # Prevents direct modification of the snake's body.
        return self.__body.copy()

    def set_head(self, x, y):
        self.__head = (x, y)

    def get_direction(self):
        return self.__direction

    def get_color(self):
        return self.__color

    def set_direction(self, x, y):
        self.__direction = (x, y)
        
    def set_body(self, index, x, y):
            if (index >= len(self.get_body())):
                self.__body.append((x,y))
            else:
                self.__body[index] = (x, y)

    def removeLastTail(self):
            return self.__body.pop(len(self.get_body())-1)
        

    def get_snake_speed(self):
        return self.__snake_speed

    def get_food_eaten(self):
        return self.__foodEaten

    def increase_food_eaten(self):
        self.__foodEaten += 1

    def get_starting_lenght(self):
            return self.__startingBodyLenght

    snakeSpeed = SnakeSpeed()

    def snakeUpdate(self, cells_per_sec):
        self.cells_per_sec = cells_per_sec
        if(self.snakeSpeed.update(self.cells_per_sec)):
            self.snake_move()
            self.snakeBodyMovement()
            self.ouroboros()       

    def snake_move(self):                
        self.set_head(self.get_head()[0] + self.get_direction()[0], self.get_head()[1] + self.get_direction()[1])

    def snakeBodyMovement(self):
        for i in (range(self.get_food_eaten() + self.get_starting_lenght(), -1, -1)):
            if not(i == 0):
                self.set_body(i, self.get_body()[i-1][0], self.get_body()[i-1][1])
                continue

            self.set_body(i, self.get_head()[0], self.get_head()[1])
            if(len(self.get_body()) -1 > self.get_food_eaten() + self.get_starting_lenght()):
                self.removeLastTail()

    def ouroboros(self):
        hitSelf = False
        for i in range(len(self.get_body())-1):
            if(snake_hits_itself(self.get_head(), self.get_body()[i+1], False)):
                hitSelf = True
        return hitSelf


    def get_speed(self):
        return self.__speed

    speed_controller = SnakeSpeed()

    