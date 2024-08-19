points = 0
games = []
draws = []
for i in range(0, 8):
  line = input().split(' v ')
  games.append(line)

for i in range(0, 8):
  [home, away] = [int(x) for x in input().split()]
  if (home == away):
    if (home > 0):
      points = points + 3
      draws.append(games[i])
      continue
    points = points + 2
    continue
  points = points + 1

print(points)

for g in draws:
  print(g[0], " v ", g[1])

