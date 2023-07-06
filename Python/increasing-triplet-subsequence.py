from ast import List
from math import inf

def increasingTriplet(self, nums: List[int]) -> bool:
  first, second = inf, inf
  for third in nums:
    if second < third:
      return True
    elif third <= first:
      first = third
    elif third <= second:
      second = third
  return False