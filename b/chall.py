print(input())

[dollars, cents] = [int(x) for x in input().split()]

thresh = int(input())

for i in range(0, int(input())):
  line = input()
  buy = int(line)
  free = (buy // thresh)
  if ((free * thresh) + free > buy):
    free = free - 1
  print("Buy " + str(buy) + ", pay for " + str(buy - free) + ", get " + str(free) + " free. Save $" + '{0:.2f}'.format(((dollars + (cents / 100)) * free * 100) / 100) + ".")