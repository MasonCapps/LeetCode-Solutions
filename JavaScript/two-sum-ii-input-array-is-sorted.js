var twoSum = function(numbers, target) {
  for (let low = 0, high = numbers.length - 1; low < high;) {
    if (numbers[low] + numbers[high] > target) {
      high--;
    } else if (numbers[low] + numbers[high] < target) {
      low++;
    } else {
      return [low + 1, high + 1];
    }
  }
};