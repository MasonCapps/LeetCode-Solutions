var reverseWords = function(s) {
  const splitString = s.split(" ");
  for (let i = 0; i < splitString.length; i++) {
    const finalIndex = splitString[i].length - 1;
    const reversedWord = [];
    let word = splitString[i];
    for (let j = splitString[i].length - 1; j >= 0; j--) {
      reversedWord.push(word[j]);
    }
    splitString[i] = reversedWord.join("");
  }
  return splitString.join(" ");
};