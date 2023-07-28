var maxProfit = function(prices) {
  let currentMaxProfit = 0;
  let minimum = prices[0];
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < minimum) {
      minimum = prices[i];
    } else if (prices[i] - minimum > currentMaxProfit) {
      currentMaxProfit = prices[i] - minimum;
    }
  }
  return currentMaxProfit;
};
