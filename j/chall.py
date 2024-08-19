# Snaggle
def evaluateExpression(exp: str):
  try: 
    if exp[0] == "(":                           # Checks if the expression has a bracket
      exp = exp[1:len(exp):1]                   # Remove the bracket
    else:
      raise Exception                           # If the expression doesn't have a bracket it's an integer
  except:                                       # Handle integer expression
    numBrackets = exp.split(" ")[0].find(')')   # Count the number of closing brackets in component of the expression 
    if (numBrackets > -1):                      # If there are any, replace them all. 
                                                # i.e. the expression: 200) -1000) would be split into ['200)', '-1000)']
                                                # we would remove the bracket from '200)' > '200' so that we can parse it and return the remaining expression
      exp = exp.replace(')', '', numBrackets)
    arr = exp.split(' ')
    return [float(arr[0]), ' '.join(arr[1::])]  # Parses the first index in the expression and returns the rest
  
                                                # Here means we are in a snaggle expression (not an integer)
  [p, exp] = evaluateExpression(exp)            # Will parse p from the expression (we can guarantee this part of the expression is integer p)
  [e1, exp] = evaluateExpression(exp)           # Will attempt to evaluate the expression at e1 (might be an integer, or a snaggle expression)
  [e2, _] = evaluateExpression(exp)             # Will attempt to evaluate the remaining part of the expression (might be an integer, or a snaggle expression)

  remain = ' '.join(exp.split(" ")[1::])        # If we a solving a nested expression, the nested expression will be replaced with it's value
                                                # The remaining expression will continue to be parsed
  return [solveExpression(float(p), float(e1), float(e2)), remain]

def solveExpression(p: float, x: float, y: float):
  return ((p * (x + y)) + ((1 - p) * (x - y)))

while (True):
  expression = input()
  if expression  == "()":
    break
  print('{0:.2f}'.format(evaluateExpression(expression)[0]))