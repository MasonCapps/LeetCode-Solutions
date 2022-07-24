var preorder = function(root) {
  const traversedArray = [];
  const stack = [];
  
  if (!root) {
    return traversedArray;
  }
  
  stack.push(root);
  while (stack.length) {
    const curr = stack.pop();
    traversedArray.push(curr.val);
    for (let i = curr.children.length - 1; i >= 0; i--) {
      stack.push(curr.children[i]);
    }
  }
  return traversedArray;
};