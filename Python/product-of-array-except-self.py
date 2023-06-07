from ast import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
  pre = 1
  post = 1
  result = [1] * len(nums)

  for i in range(len(nums)):
    result[i] *= pre
    pre *= nums[i]
    result[len(result) - i - 1] *= post
    post *= nums[len(nums) - i - 1]
  return result