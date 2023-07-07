from ast import List

def maxOperations(self, nums: List[int], k: int) -> int:
  nums.sort()
  count = 0
  start, end = 0, len(nums) - 1
  
  while start < end:
    if nums[start] + nums[end] > k:
      end -= 1
    elif nums[start] + nums[end] < k:
      start += 1
    else:
      count += 1
      start += 1
      end -= 1 
  return count