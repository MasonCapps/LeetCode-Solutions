var moveZeroes = function(nums) {
  let indexPlacer = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      [nums[i], nums[indexPlacer]] = [nums[indexPlacer], nums[i]];
      indexPlacer++;
    }
  }
};