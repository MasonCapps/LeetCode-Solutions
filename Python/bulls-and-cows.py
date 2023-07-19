def getHint(self, secret: str, guess: str) -> str:
  cow_hash = {}
  for i in secret:
    if i in cow_hash:
      cow_hash[i] += 1
    else:
      cow_hash[i] = 1
  
  cow_count = 0
  for i in guess:
    if i in cow_hash and cow_hash[i] != 0:
      cow_count += 1
      cow_hash[i] -= 1

  bull_count = 0
  for i in range(len(guess)):
    if guess[i] == secret[i]:
      bull_count += 1
      cow_count -= 1
  return f'{bull_count}A{cow_count}B'