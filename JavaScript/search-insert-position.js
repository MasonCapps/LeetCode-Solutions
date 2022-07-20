var searchInsert = function(nums, target) {
  let low = 0;
  let high = nums.length - 1;
  if (target > nums[high]) {
    return nums.length;
  } else if (target < nums[low]) {
    return 0;
  }
  while (low <= high) {
    let middle = parseInt((low + high) / 2);
    if (nums[middle] === target) {
      return middle;
    } else if (nums[middle] < target) {
      if (nums[middle + 1] > target) {
        return middle + 1;
      } else {
        low = middle + 1;
      }
    } else if (nums[middle] > target) {
      if (nums[middle - 1] < target) {
        return middle;
      } else {
        high = middle - 1; 
      }
    }
  }
};