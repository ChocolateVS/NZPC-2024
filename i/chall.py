from typing import List
[H, W] = [int(x) for x in input().split()]

rows = []

for i in range(0, H):
  rows.append([int(x) for x in input().split()]) 

cells = dict()
memo = dict()
sinks = dict()
chars = dict()

def getLowest(cell: List[int]):
  lowest = cell
  x = cell[0]
  y = cell[1]
  memory = memo.get(str(x) + " " + str(y))
  if (memory != None):
    return memory

  if (y - 1 >= 0 and rows[x][y] > rows[x][y - 1]):
    lowest = [x, y - 1]
  
  if (x - 1 >= 0 and rows[x - 1][y] < rows[lowest[0]][lowest[1]] and rows[x][y] > rows[x - 1][y]):
    lowest = [x - 1, y]
  
  if (x + 1 < H and rows[x + 1][y] < rows[lowest[0]][lowest[1]] and rows[x][y] > rows[x + 1][y]):
    lowest = [x + 1, y]
  
  if (y + 1 < W and rows[x][y + 1] < rows[lowest[0]][lowest[1]] and rows[x][y] > rows[x][y + 1]):
    lowest = [x, y + 1]

  if (x == lowest[0] and y == lowest[1]):
    memo[str(x) + " " + str(y)] = lowest
    return lowest

  else:
    lowest = getLowest(lowest)
    memo[str(x) + " " + str(y)] = lowest
    return lowest


for x in range(0, H):
  for y in range(0, W):
    lowest = getLowest([x, y])
    print('Check Point', memo)
    cells[str(x) + " " + str(y)] = str(lowest[0]) + str(lowest[1])

char = 'a'

for c in cells.items():
  if (sinks.get(c[1]) == None):
    sinks[c[1]] = char
    char = chr(ord(char) + 1)

  chars[c[0]] = sinks.get(c[1])

for x in range(0, H):
  output = ""
  for y in range(0, W):
    output = output + chars[str(x) + " " + str(y)]
  print(output)
