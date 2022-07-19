var runningSum = function(nums) {
  let runningSumArray = [];
  let runningSum = 0;
  nums.forEach(function (number) {
    runningSum += number;
    runningSumArray.push(runningSum);
  });
  return runningSumArray;
};