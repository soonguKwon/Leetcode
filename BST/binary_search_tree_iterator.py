# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        import collections
        self.dq = collections.deque()

        def dfs(node: TreeNode):
            if node is None: return

            dfs(node.left)
            self.dq.append(node.val)
            dfs(node.right)

        dfs(root)
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.dq.popleft()
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.dq)
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()