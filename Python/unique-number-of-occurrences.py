from ast import List

def uniqueOccurrences(self, arr: List[int]) -> bool:
  hash = {}
  for i in arr:
    if i in hash:
      hash[i] += 1
    else:
      hash[i] = 1
  count_array = []
  for i in hash.values():
    if i in count_array:
      return False
    count_array.append(i)
  return True