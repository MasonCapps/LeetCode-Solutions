var reverseString = function(s) {
  const lastIndex = s.length - 1;
  for (let i = 0; i < s.length / 2; i++) {
    [s[i], s[lastIndex - i]] = [s[lastIndex - i], s[i]];
  } 
};