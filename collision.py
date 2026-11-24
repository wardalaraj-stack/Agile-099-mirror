def position_is_occupied(position, occupied_positions):
    #is the position opcubied by snake/obstical/enemy/otherplayer 
    return position in occupied_positions


def snake_hits_itself(next_head, body, growing=False):
    #cheak for the snake hitting itself if growing agenst all body
    #if not growing agent all body -tail
    occupied_body = body if growing else body[:-1]
    return position_is_occupied(next_head, occupied_body)


def hits_obstacle(next_head, obstacles):
    #futer collision with obstical 
    return position_is_occupied(next_head, obstacles)


def hits_snake(next_head, other_head, other_body):
    #future collision with another player
    return position_is_occupied(next_head, [other_head, *other_body])
