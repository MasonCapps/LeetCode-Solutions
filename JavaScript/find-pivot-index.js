var pivotIndex = function(nums) {
  for (let pivotIndex = 0; pivotIndex < nums.length; pivotIndex++) {
    let leftSum = 0;
    let rightSum = 0;
    for (let i = 0; i < pivotIndex; i++) {
      leftSum += nums[i];
    }
    for (let i = 0; i < nums.length; i++) {
      if (i > pivotIndex) {
        rightSum += nums[i];
      }
    }
    if (leftSum === rightSum) {
      return pivotIndex;
    }
  }
  return -1;
};