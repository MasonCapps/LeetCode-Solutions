def isAnagram(self, s: str, t: str) -> bool:
  hash_s, hash_t = {}, {}
  for letter in s:
    if letter in hash_s:
      hash_s[letter] += 1
    else:
      hash_s[letter] = 1
  for letter in t:
    if letter in hash_t:
      hash_t[letter] += 1
    else:
      hash_t[letter] = 1
  return hash_s == hash_t