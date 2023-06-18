from ast import List

def largestAltitude(self, gain: List[int]) -> int:
  altitude = 0
  altitudes = [altitude]
  for i in gain:
    altitude += i
    altitudes.append(altitude)
  return max(altitudes)