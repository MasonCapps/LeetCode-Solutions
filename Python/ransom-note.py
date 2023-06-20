def canConstruct(self, ransomNote: str, magazine: str) -> bool:
  letter_hash = {}
  for i in magazine:
    if i in letter_hash:
      letter_hash[i] += 1
    else:
      letter_hash[i] = 1

  for i in ransomNote:
    if i not in letter_hash or letter_hash[i] < 1:
      return False
    else:
      letter_hash[i] -= 1
  return True