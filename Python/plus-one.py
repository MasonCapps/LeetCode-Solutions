from ast import List

def plusOne(self, digits: List[int]) -> List[int]:
  string_digits = ""
  for i in digits:
    string_digits += str(i)
  number = int(string_digits) + 1

  result = []
  for digit in str(number):
    result.append(int(digit))
  return result