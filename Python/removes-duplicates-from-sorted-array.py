from ast import List

def removeDuplicates(self, nums: List[int]) -> int:
  unique_hash = {}
  i = 0

  while i < len(nums):
    if nums[i] not in unique_hash:
      unique_hash[nums[i]] = 1
    else:
      nums.remove(nums[i])
      i -= 1
    i += 1
  return len(nums)