# Daniel Chen
# Double Dice
# 1 April 2019

rounds = int(input('Rounds: '))

player1 = 100
player2 = 100

for x in range(rounds):
    bothplayers = input('Round ' + str(x + 1) + ': ')
    player1score = int(bothplayers[0])
    player2score = int(bothplayers[2])
    if player1score > player2score:
        player2 = player2 - player1score
    elif player2score > player1score:
        player1 = player1 - player2score

print(player1)
print(player2)
        