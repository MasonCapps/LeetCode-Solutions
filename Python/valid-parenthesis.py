def isValid(self, s: str) -> bool:
  stack = []
  for bracket in s:
    if bracket in '({[':
      stack.append(bracket)
    elif stack:
      compare = stack.pop()
      if bracket == ')' and compare != '(' or bracket == '}' and compare != '{' or bracket == ']' and compare != '[':
        return False
    else:
      return False
      
  if stack:
    return False
  else:
    return True