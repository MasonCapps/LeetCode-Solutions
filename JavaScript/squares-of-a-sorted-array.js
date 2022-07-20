var sortedSquares = function(nums) {
  let squaredArray = [];
  nums.forEach(function(number) {
    squaredArray.push(number * number);
  });
  let count = 0;
  for (let i = 0; i < squaredArray.length; i++) {
    if (squaredArray[i] >= squaredArray[i + 1]) {
      let elementSwapper = squaredArray[i]
      squaredArray[i] = squaredArray[i + 1];
      squaredArray[i + 1] = elementSwapper;
    } else if (count > squaredArray.length) {
      break;
    } else {
      i = -1;
      count++;
    }
  }
  return squaredArray;
};