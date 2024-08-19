[H, K] = [int(x) for x in input().split()]

heads = []
knights = []

for i in range(0, H):
  heads.append(int(input()))

for i in range(0, K):
  knights.append(int(input()))

heads.sort()
knights.sort()

cost = 0

while (len(heads) > 0):
    if (len(knights) == 0):
      print("Loowater is doomed!")
      break
      
    if (knights[0] >= heads[0]):
      cost += knights[0]
      knights.pop(0)
      heads.pop(0)
      continue
    
    knights.pop(0)
  
print(cost)