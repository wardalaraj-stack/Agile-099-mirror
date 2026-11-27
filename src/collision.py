import random


def position_is_occupied(position, occupied_positions):
    #is the position opcubied by snake/obstical/enemy/otherplayer 
    return position in occupied_positions


def snake_hits_itself(next_head, body, growing=False):
    #cheak for the snake hitting itself if growing agenst all body
    #if not growing agent all body -tail
    #occupied_body = body if growing else body[:-1]
    # return position_is_occupied(next_head, occupied_body)
    if(next_head == body):
        return True
    else:
        return False
        
def food_collision(foodPos, snakeHead):
    if(foodPos == snakeHead):
        return True
    else:
        return False

def hits_obstacle(next_head, obstacles):
    #futer collision with obstical 
    return position_is_occupied(next_head, obstacles)


def hits_snake(next_head, other_head, other_body):
    #future collision with another player
    return position_is_occupied(next_head, [other_head, *other_body])


def random_position(board):
    return (random.randrange(0, board.width), random.randrange(0, board.height))


def find_free_spot(board, snake_head, snake_body):
    occupied = [snake_head] + snake_body
    position = random_position(board)
    while position_is_occupied(position, occupied):
        position = random_position(board)
    return position

def hits_border(next_head, board):
    # Check if the snake's head is outside the board
    if board.contains(next_head):
        return False
    else:
        return True
