allhex = "0123456789ABCDEF"
words = ""
hexChars = []
nums = []
for x in range(0, int(input())):
  line = input().split(' ')
  hex = ""
  for x in line:
    if (allhex.find(x) < 0):
      words = words + x
      if (len(hex) >  0):
        hexChars.append(hex)
      hex = ""
      continue
    hex = hex + x
  if (len(hex) >  0):
    hexChars.append(hex)


for x in hexChars:
  nums.append(int('0x' + x, 16))

print(words)
for n in nums:
  print(n)