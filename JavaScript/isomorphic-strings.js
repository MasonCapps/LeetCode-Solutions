var isIsomorphic = function(s, t) {
  let checker = true;
  if (s === t) {
    return true;
  } 
  for (let i = 0; i < s.length; i++) {
    for (let j = 0; j < s.length; j++) {
      if (s[i] === s[j] && i !== j) {
        if (t[i] === t[j]) {
          checker = true;
        } else {
          return false;
        }
      } else if (t[i] === t[j] && i !== j) {
        if (s[i] === s[j]) {
          checker = true;
        } else {
          return false;
        }
      } 
    }
  }
  return checker;
};