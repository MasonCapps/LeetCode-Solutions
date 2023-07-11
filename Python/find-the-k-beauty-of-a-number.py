def divisorSubstrings(self, num: int, k: int) -> int:
  string = str(num)
  count = 0
  window = string[:k]
  
  for i in range((len(string) - k) + 1):
    if int(window) != 0 and num % int(window) == 0:
      count += 1
    window = string[i + 1:k + i + 1]
  return count