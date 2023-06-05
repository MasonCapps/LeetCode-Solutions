from ast import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
  anagram_groups = {}

  for string in strs:
    sorted_string = "".join(sorted(string))
    if sorted_string not in anagram_groups:
      anagram_groups[sorted_string] = []
    anagram_groups[sorted_string].append(string)
    
  return anagram_groups.values()