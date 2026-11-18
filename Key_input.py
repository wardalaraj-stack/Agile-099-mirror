import snake
import pygame

class KeyInput:

    def __init__(self):
        self.__currentDirection = (1,0)
        self.__direction = {
            pygame.K_UP: (0,-1),
            pygame.K_DOWN: (0,1),
            pygame.K_LEFT: (-1,0),
            pygame.K_RIGHT: (1,0),
        }

    def get_direction(self):
        return self.__currentDirection

    def set_direction(self, event):
        if event.type == pygame.KEYDOWN and event.key in self.__direction:
            self.__currentDirection = self.__direction[event.key]
