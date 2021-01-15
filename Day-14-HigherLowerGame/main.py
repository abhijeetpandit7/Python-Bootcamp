import random
import subprocess
from game_data import data
from art import logo,vs

def newRound(teamA, teamB):
    subprocess.call("cls", shell=True)
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {teamA['name']}, a {teamA['description']} from {teamA['country']}")
    print(vs)
    print(f"Against B: {teamB['name']}, a {teamB['description']} from {teamB['country']}")
    if teamA['follower_count'] > teamB['follower_count']:
        return 'a'
    return 'b'

gameOn = True
score = 0
teamA = random.choice(data)
while gameOn:
    teamB = random.choice(data)
    if teamA == teamB:
        teamB = random.choice(data)
    winner = newRound(teamA, teamB)
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == winner:
        score += 1
        teamA = teamB
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        gameOn = False