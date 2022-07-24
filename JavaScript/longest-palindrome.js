var longestPalindrome = function(s) {
  let letterHash = {};
  let count = 0;
  
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    if (letterHash[char]) {
      letterHash[char] += 1;
      if (letterHash[char] % 2 === 0) {
        count += 2;
      }
    } else {
      letterHash[char] = 1;
    }
  }
  
  if (s.length === count) {
    return count;
  } else {
    return count + 1; 
  }
};