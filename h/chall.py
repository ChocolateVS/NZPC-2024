import math

halfTurn = False

def swapPlayers(player1, player2):
  tmp = player1
  player1 = player2
  player2 = tmp
  return player1, player2

def printHandicap(name1, name2, handicap):
  print(name1, 'recieves', handicap, 'free turns from', name2)

def getHandicaps(p1, p2):
  global halfTurn
  if (p1[1] > p2[1]):
    [p1, p2] = swapPlayers(p1, p2)
  if (halfTurn == True):
    handicap =(p2[1] - p1[1]) // 2
  else:
    handicap = (p2[1] - p1[1]) // 2
    if (handicap % 1 > 0):
      halfTurn = True
      handicap = math.ceil(handicap)
  printHandicap(p2[0], p1[0], handicap)

player1 = input().split()
player2 = input().split()
player3 = input().split()
player4 = input().split()

player1[1] = int(player1[1])
player2[1] = int(player2[1])
player3[1] = int(player3[1])
player4[1] = int(player4[1])

if (player1[1] < player2[1]):
  [player1, player2] = swapPlayers(player1, player2)

if (player3[1] > player4[1]):
  [player3, player4] = swapPlayers(player3, player4)

print(player1, player2, player3, player4)
getHandicaps(player2, player4)
getHandicaps(player1, player3)


