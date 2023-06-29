from ast import List

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
  boolean_array = []
  for i in candies:
    if i + extraCandies >= max(candies):
      boolean_array.append(True)
    else:
      boolean_array.append(False)
  return boolean_array