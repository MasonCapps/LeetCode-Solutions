var isSubsequence = function(s, t) {
  let letter = 0;
  for (let i = 0; i < t.length; i++) {
    if (s[letter] === t[i]) {
      letter++;
    }
  }
  if (letter === s.length) {
    return true;
  } else {
    return false;
  }
};