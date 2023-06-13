from ast import List

def equalPairs(self, grid: List[List[int]]) -> int:
  count = 0
  compare_array = []
  index = 0
  while index < len(grid):
    for i in range(len(grid)):
      compare_array.append(grid[i][index])
    count += grid.count(compare_array)
    
    compare_array = []
    index += 1
  return count