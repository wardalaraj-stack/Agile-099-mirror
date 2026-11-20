
import pygame
from snake import Snake
from snake_renderer import SnakeRenderer

pygame.init()
screen = pygame.display.set_mode((800, 600))

snake = Snake(5, 3)
renderer = SnakeRenderer(20)

renderer.draw_head(screen, snake)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

