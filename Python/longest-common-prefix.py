from ast import List

def longestCommonPrefix(self, strs: List[str]) -> str:
  common_prefix = ""
  sorted_strings = sorted(strs)
  first, last = sorted_strings[0], sorted_strings[-1]
  small_length = min(len(first), len(last))

  for i in range(small_length):
    if first[i] != last[i]:
      return common_prefix
    common_prefix += first[i]
  return common_prefix