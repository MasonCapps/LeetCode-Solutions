from ast import List
from collections import Counter

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
  counter = Counter(nums)
  most_frequent = counter.most_common(k)
  max_array = []

  for element in most_frequent:
    max_array.append(element[0])
  return max_array