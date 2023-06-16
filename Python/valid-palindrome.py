def isPalindrome(self, s: str) -> bool:
  string = ''.join(filter(str.isalnum, s))
  string = string.lower()

  i = 0
  j = len(string) - 1
  while i < j:
    if string[i] != string[j]:
      return False
    i += 1
    j -= 1
  return True