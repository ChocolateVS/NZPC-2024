[width, height] = [int(x) for x in input().split()]

items = dict()

for i in range(0, int(input())):
  [x, y] = [int(x) for x in input().split()]
  key = int(str(x) + str(y))
  if (items.get(key) == None):
    items[key] = 0
  
  items[key] = items[key] + 1

found = 0

for i in range(0, int(input())):
  [x, y] = [int(x) for x in input().split()]

  key = int(str(x) + str(y))

  if (items.get(key) != None):
    found = found + items.get(key)

print(found)