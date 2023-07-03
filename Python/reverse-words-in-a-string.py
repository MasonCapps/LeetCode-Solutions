def reverseWords(self, s: str) -> str:
  array = s.split()
  i, j = 0, len(array) - 1
  while i < j:
    array[i], array[j] = array[j], array[i]
    i += 1
    j -= 1
  return " ".join(array)