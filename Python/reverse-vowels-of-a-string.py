def reverseVowels(self, s: str) -> str:
  vowels = []
  vowel_check = "aeiouAEIOU"
  for i in s:
    if i in vowel_check:
      vowels.append(i)
  result = ""
  for i in s:
    if i in vowel_check:
      result += vowels[-1]
      vowels.pop()
    else:
      result += i
  return result