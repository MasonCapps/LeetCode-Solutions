from ast import List

def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
  if n == 0:
    return True
  for i in range(len(flowerbed)):
    if i == len(flowerbed) - 1:
      if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
        n -= 1
    elif i == 0:
      if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
        n -= 1
        flowerbed[i] = 1
    else:
      if flowerbed[i] == 0:
        if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
          n -= 1
          flowerbed[i] = 1
    if n == 0:
      return True
  return False