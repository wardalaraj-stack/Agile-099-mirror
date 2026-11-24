import pygame

MARKER_INSET = 6

class Food_drawing:

    def Draw_food(surface, view, food):
        rect = view.cell_rect(food.getFood()).inflate(-2 * MARKER_INSET, -2 * MARKER_INSET)
        pygame.draw.ellipse(surface,food.getColor(), rect)
