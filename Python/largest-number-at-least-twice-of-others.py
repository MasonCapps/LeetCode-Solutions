from ast import List

def dominantIndex(self, nums: List[int]) -> int:
  max_index = 0
  second_max = min(nums)
  
  for i in range(len(nums)):
    if nums[i] == max(nums):
      max_index = i
    elif nums[i] > second_max:
      second_max = nums[i]
      
  if max(nums) / 2 >= second_max:
    return max_index
  else:
    return -1