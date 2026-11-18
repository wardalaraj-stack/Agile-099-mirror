import pygame
from snake import Snake
from snake_renderer import SnakeRenderer
from Key_input import KeyInput


screen = pygame.display.set_mode((600, 400))
key_input = KeyInput()
snake = Snake(5, 5)
renderer = SnakeRenderer(20)

running = True
while running:
    for event in pygame.event.get():
        key_input.set_direction(event)
        if event.type == pygame.QUIT:
            running = False

    snake.set_direction(*key_input.get_direction())
    print(snake.get_direction())
    screen.fill((0, 0, 0))
    renderer.draw_head(screen, snake)
    pygame.display.flip()

pygame.quit()