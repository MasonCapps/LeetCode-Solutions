from ast import List

def summaryRanges(self, nums: List[int]) -> List[str]:
  if len(nums) == 0:
    return []
  
  range_array = []
  low_range = nums[0]
  for i in range(1, len(nums)):
    if nums[i] != nums[i-1] + 1:
      if low_range == nums[i-1]:
        range_array.append(f'{low_range}')
      else:
        range_array.append(f'{low_range}->{nums[i - 1]}')
      low_range = nums[i]

  if low_range == nums[-1]:
    range_array.append(f'{low_range}')
  else:
    range_array.append(f'{low_range}->{nums[-1]}')

  return range_array