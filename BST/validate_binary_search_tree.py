# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def nodeCheck(node: TreeNode, min, max):
            if node.val <= min:
                return False
            if node.val >= max:
                return False

            left_ok = True
            right_ok = True

            if node.left is not None:
                left_ok = nodeCheck(node.left, min, node.val)
            if node.right is not None:
                right_ok = nodeCheck(node.right, node.val, max)

            return left_ok and right_ok

        if root is None:
            return True

        return nodeCheck(root, float('-inf'), float('inf'))