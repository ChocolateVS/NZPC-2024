for i in range(0, int(input())):
  year = int(input())
  type = ''
  when = ''
  if (year == 2024):
    when = "is"
  if (year > 2024):
    when = "will be"
  if (year < 2024):
    when = "was"

  if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    type = "leap"
  else:
    type = "common"
    
  print(str(year) + " " + when + " a " + type + " year.")

