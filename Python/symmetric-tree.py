def isSymmetric(self, root: Optional[TreeNode]) -> bool:
  def dfs(left, right):
    if not left and not right:
      return True
    elif not left or not right:
      return False
    else:
      return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
  return dfs(root.left, root.right)