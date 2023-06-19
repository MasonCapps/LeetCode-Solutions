from ast import List

def removeDuplicates(self, nums: List[int]) -> int:
  nums_hash = {}
  i = 0
  while i < len(nums):
    if nums[i] in nums_hash:
      if nums_hash[nums[i]] == 2:
        nums.pop(i)
        i -= 1
      else:
        nums_hash[nums[i]] += 1
    else:
      nums_hash[nums[i]] = 1
    i += 1