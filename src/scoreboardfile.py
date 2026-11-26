import random
import json
import os 


#global variables
playerName = str(input('Enter your name > '))
score = random.randint(0,2000)
filename = 'scoreboard.json'



def score_storage(playerName, score):
    with open(filename, 'a') as file:
        file.write(f'{playerName} > {str(score)}; \n')
        file.close

def leaderboard():
    with open(filename, 'r') as file:
    scores = []

    for line in file:
        updatedList = line.split(';')
        if len(updatedList)==3:
            playerName = updatedList[0]
            playerScore = int(updatedList[1])
            scores.append(playerName, playerScore)
    file.close()

    sortedScores = sorted(scores, key=lambda sort:sort[1])

    del sortedScores [5:]

    print('--Leaderboard--')
    place = 1
    for score in sortedScores:
        print(f'{str(place)}: {str(score[1])}')
        place = place + 1

score_storage(playerName, score)
leaderboard()