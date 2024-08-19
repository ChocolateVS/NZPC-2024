while (True):
  nums = input()
  if (nums == '0'):
    break

  multiple = 2
  sum = 0
  for num in nums[::-1]:
    sum = sum + int(num) * multiple
    multiple = multiple + 1
  
  result = 11 - (sum % 11)

  check = nums
  if (result == 11):
    check = check + '0'
  if (result > 0 and result < 10):
    check = check + str(result)
  if (result == 10):
    check = 'rejected'

  print(nums, '->', check)