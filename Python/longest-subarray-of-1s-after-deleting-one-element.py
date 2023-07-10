from ast import List

def longestSubarray(self, nums: List[int]) -> int:
  total_max = 0
  start = 0
  zero_count = 0
  for end in range(len(nums)):
    if nums[end] == 0:
      zero_count += 1
    if zero_count > 1:
      if nums[start] == 0:
        zero_count -= 1
      start += 1
    total_max = max(total_max, (end - start))
  
  if total_max == len(nums):
    return total_max - 1
  else:
    return total_max