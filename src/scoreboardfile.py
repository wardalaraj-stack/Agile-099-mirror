import random
import json
import pygame
#from src import board_view, snake, Food, board, board_launch
from src.snake import Snake
from src.board import Board
from src.board_view import BoardView
from src.Food import Food
import src.board_launch

test_score = src.board_launch.main()
print(test_score)

#print(score)

#global variables
#board = Board(width=40, height=20, cell_size=32)
# #board_view = BoardView(board, offset=(20, 20))
#headPos = snake()s#oodPos = Food()

headPos = snake.get_head()
foodPos = Food.getFood()
#clock = pygame.time.Clock()
#font = pygame.font.Font(None, 28)



# score display
def single_score():
    score = 0
    if headPos == foodPos:
        score += 5
    return score
    print(score)


playerName = str(input('Enter your name > '))
filename = 'leaderboard.json'


def score_storage(playerName, score):
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(f'{playerName} > {str(score)}; \n')

def leaderboard():
    scores = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            playerName, score = line.strip().removesuffix(";").rsplit(" > ", 1)
            scores.append([playerName, int(score)])
    
    topScores = sorted(scores, key=lambda sort:sort[1], reverse = True)[:5]

    with open('leaderboard.json', 'w', encoding="utf-8") as output_file:
        json.dump(topScores, output_file)

    print('--Leaderboard--')
    place = 1
    for score in topScores:
        place = place + 1
    return topScores

score_storage(playerName, score)
leaderboard()