import random

playerName = input('Enter your name > ')
score = random.randint(0,2000)

def score_storage(playerName, score):
    file = open('scoreboard.txt', 'a')
    file.write(f'{playerName} > {str(score)}; \n')
    file.close()

def leaderboard():
    file = open('scoreboard.txt', 'r')
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