def wordPattern(self, pattern: str, s: str) -> bool:
  string_array = s.split(' ')
  string_set = set(string_array)
  pattern_set = set(pattern)

  if len(string_set) != len(pattern_set) or len(string_array) != len(pattern):
    return False
  else:
    pattern_hash = {}
    for i in range(len(pattern)):
      if pattern[i] not in pattern_hash:
        pattern_hash[pattern[i]] = string_array[i]
        
    for i in range(len(pattern)):
      if pattern_hash[pattern[i]] != string_array[i]:
        return False
    return True