
class Food:
   
    def __init__(self, x, y):
        self.__color = (255, 0, 0)
        self.__currentPosition = (x, y)

    def newFood(self, x, y):
        self.setFood(x, y)

    def getFood(self):
        return self.__currentPosition

    def getColor(self):
        return self.__color

    def setFood(self, x, y):
        self.__currentPosition = (x, y)
