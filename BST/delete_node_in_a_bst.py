# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None: return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None: return root.right
            elif root.right is None: return root.left

            minNode = root.right

            while (minNode.left is not None):
                minNode = minNode.left

            root.val = minNode.val
            root.right = self.deleteNode(root.right, root.val)
        return root