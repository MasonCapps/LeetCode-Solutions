def isPalindrome(self, x: int) -> bool:
  num_string = str(x)
  j = len(num_string) - 1
  for i in range(len(num_string)):
    if num_string[i] != num_string[j]:
      return False
    j -= 1
  return True