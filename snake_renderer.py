
import pygame

class SnakeRenderer:
    """Draws the snake head using Pygame."""

    def __init__(self, cell_size):
        self.__cell_size = cell_size
    
    def get_pixel_position(self, x, y):
        """Convert grid coordinates to pixel coordinates."""
        x_position = x * self.__cell_size
        y_position = y * self.__cell_size

        return x_position, y_position
    
    def draw_head(self, surface, snake):
        x, y = snake.get_head()
        pixel_x, pixel_y = self.get_pixel_position(x, y)

        color = snake.get_color()

        rect = pygame.Rect(
                pixel_x,
                pixel_y,
                self.__cell_size,
                self.__cell_size
        )

        pygame.draw.rect(surface, color, rect)

