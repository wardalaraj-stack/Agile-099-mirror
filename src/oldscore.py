import json
from src import board_launch

#global variables
playerName = str(input('Enter your name > '))
filename = 'leaderboard.json'

test_score = board_launch.main()
print(test_score)

def score_storage(playerName, score):
    """Stores score :))"""
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(f'{playerName} > {str(score)}; \n')

def leaderboard():
    scores = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            playerName, playerScore = line.strip().removesuffix(";").rsplit(" > ", 1)
            scores.append([playerName, int(playerScore)])
    
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
