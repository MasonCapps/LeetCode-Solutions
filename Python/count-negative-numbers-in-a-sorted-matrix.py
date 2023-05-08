from ast import List

def countNegatives(self, grid: List[List[int]]) -> int:
  count = 0
  for array in grid:
    for i in range(len(array)):
      if array[i] < 0:
        count += len(array) - i
        break
  return count