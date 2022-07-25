var solution = function(isBadVersion) {
  return function(n) {
    let low = 1;
    let high = n;
    
    while (low < high) {
      let middle = parseInt((low + high) / 2);
      if (isBadVersion(middle)) {
        high = middle;
      } else {
        low = middle + 1;
      }
    }
    return low;
  };
};