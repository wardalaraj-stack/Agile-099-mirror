import pygame
import random


from src.key_input import KeyInput
from src.snake import Snake
from src.board import Board
from src.board_view import BoardView
from src.Food import Food
from src.Food_drawing import Food_drawing
from src.collision import random_position, find_free_spot, food_collision, hits_border

SNAKE_HEAD_INSET = 6
MARKER_COLOR = (36, 91, 149)
MARKER_INSET = 6

def draw_snake_head(surface, board_view, head_position, head_color):
    head_rect = board_view.cell_rect(head_position).inflate(
        -2 * SNAKE_HEAD_INSET,
        -2 * SNAKE_HEAD_INSET
    )
    pygame.draw.ellipse(surface, head_color, head_rect)


def draw_body(surface, view, position):
    rect = view.cell_rect(position).inflate(-2 * MARKER_INSET, -2 * MARKER_INSET)
    pygame.draw.ellipse(surface, MARKER_COLOR, rect)
    

def main():
    pygame.init()

    board = Board(width=40, height=20, cell_size=32)

    board_view = BoardView(board, offset=(20, 20))
    screen = pygame.display.set_mode((
        board_view.pixel_size[0] + 40,
        board_view.pixel_size[1] + 40,
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
        board_view.draw(screen)


        #speed of snake
        snake.snakeUpdate(snake.get_snake_speed()) 
        
        # Stop the game if the snake hits the map border
        if hits_border(snake.get_head(), board):
         break

        # Render the snake's head
        draw_snake_head(screen, board_view, snake.get_head(), snake.get_color())
       
        #Food spawining Logic
        #position = snake.get_head()     
        Food_drawing.Draw_food(screen, board_view, food)


        #draw_marker(screen, board_view, position) #draw for test marker
        for i in range(len(snake.get_body())):
            draw_body(screen, board_view, (snake.get_body()[i]))

        quit_message = font.render(
            "ESC: quit",
            True, (235, 235, 235)
        )
        screen.blit(quit_message, (20, board_view.pixel_size[1] + 27))

        pygame.display.flip()
        clock.tick(60)


        if(snake.ouroboros()):
            running = False
        if(food_collision(food.getFood(), snake.get_head())): #this is really bad, fix this
            snake.increase_food_eaten()
            freeSpot = find_free_spot(board, snake.get_head(), snake.get_body())
            food.newFood(freeSpot[0], freeSpot[1])



        # Speed of snake
       # snake.move(snake.get_speed())

    pygame.quit()


if __name__ == "__main__":
    main()
