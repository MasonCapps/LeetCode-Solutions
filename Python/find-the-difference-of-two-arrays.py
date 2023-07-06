from ast import List

def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
  hash1 = set(nums1)
  hash2 = set(nums2)
  
  result = [[], []]
  for i in hash1:
    if i not in hash2:
      result[0].append(i)
  for i in hash2:
    if i not in hash1:
      result[1].append(i)
      
  return result