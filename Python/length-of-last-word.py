def lengthOfLastWord(self, s: str) -> int:
  array = s.split(" ")
  final_word = ""
  for i in array:
    if len(i) > 0:
      final_word = i
  return len(final_word)