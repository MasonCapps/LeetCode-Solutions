from ast import List

def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
  sorted_array = sorted(arr)
  difference = abs(sorted_array[0] - sorted_array[1])
  
  for i in range(len(sorted_array) - 1):
    if abs(sorted_array[i] - sorted_array[i + 1]) != difference:
      return False
  return True