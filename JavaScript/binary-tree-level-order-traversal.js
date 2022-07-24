var levelOrder = function(root) {
  const levelArray = [];
  const stack = [];
  
  if (!root) {
    return levelArray;
  }
  
  stack.push(root);
  while (stack.length) {
    let length = stack.length;
    levelArray.push(stack.map(node => node.val));
    while (length--) {
      let node = stack.shift();
      if (node.left) {
        stack.push(node.left);
      }
      if (node.right) {
        stack.push(node.right);
      }
    }
  }
  return levelArray;
};