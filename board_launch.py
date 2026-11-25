import pygame
from Key_input import KeyInput
from snake import Snake
from board import Board
from board_view import BoardView
from Food import Food
from Food_drawing import Food_drawing
import random
from collision import food_collision
from collision import find_free_spot
from collision import random_position


#### test marker for borders#####
MARKER_COLOR = (36, 91, 149)
MARKER_INSET = 6

def next_marker_position(board, position, step):
    column, row = position
    column_step, row_step = step
    candidate = column + column_step, row + row_step
    return position if board.outside_edges(candidate) else candidate


def draw_marker(surface, view, position):
    rect = view.cell_rect(position).inflate(-2 * MARKER_INSET, -2 * MARKER_INSET)
    pygame.draw.ellipse(surface, MARKER_COLOR, rect)
#### end test marker for bordar

def draw_body(surface, view, position):
    rect = view.cell_rect(position).inflate(-2 * MARKER_INSET, -2 * MARKER_INSET)
    pygame.draw.ellipse(surface, MARKER_COLOR, rect)
    

def main():
    pygame.init()

    board = Board(width=10, height=20, cell_size=32)

    view = BoardView(board, offset=(20, 20))
    screen = pygame.display.set_mode((
        view.pixel_size[0] + 40,
        view.pixel_size[1] + 40,
    ))

    pygame.display.set_caption("Snake - Board demo")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)
    
    key_input = KeyInput()
    randomspot = random_position(board)
    snake = Snake(randomspot[0], randomspot[1])

#Food Logic
    freeSpot = find_free_spot(board, snake.get_head(), snake.get_body())
    food = Food(freeSpot[0], freeSpot[1])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            key_input.set_direction(event)
        snake.set_direction(*key_input.get_direction())
        
        screen.fill((15, 15, 18))
        view.draw(screen)                 
        snake.snakeUpdate(snake.get_snake_speed()) #speed of snake
        position = snake.get_head()     

        Food_drawing.Draw_food(screen, view, food)
        draw_marker(screen, view, position) #draw for test marker
        for i in range(len(snake.get_body())):
            draw_body(screen, view, (snake.get_body()[i]))

        message = font.render(
            "ESC: quit",
            True, (235, 235, 235)
        )
        screen.blit(message, (20, view.pixel_size[1] + 27))

        pygame.display.flip()
        clock.tick(60)

        if(snake.ouroboros()):
            running = False

        if(food_collision(food.getFood(), snake.get_head())): #this is really bad, fix this
            snake.increase_food_eaten()
            freeSpot = find_free_spot(board, snake.get_head(), snake.get_body())
            food.newFood(freeSpot[0], freeSpot[1])

    pygame.quit()


    


if __name__ == "__main__":
    main()
