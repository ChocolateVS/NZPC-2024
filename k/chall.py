[totalSimulationTime, threshold, maxSpikeDuration] = [int(x) for x in input().split()]

appliances = dict()

powerusage = []
for t in range(0, totalSimulationTime):
  powerusage.append(0)

while (True):
  [appliance, deltaT, deltaP] = [int(x) for x in input().split()]
  if (appliance + deltaT + deltaP == 0):
    break

  appliances.get(appliance)

