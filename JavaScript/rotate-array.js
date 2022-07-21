function reverseElements(array, start, end) {
  while (start < end) {
    [array[start], array[end]] = [array[end], array[start]];
    start++;
    end--;
  }
}

var rotate = function(nums, k) {
  k %= nums.length;
  nums.reverse();
  
  reverseElements(nums, 0, k - 1);
  reverseElements(nums, k, nums.length - 1);
};