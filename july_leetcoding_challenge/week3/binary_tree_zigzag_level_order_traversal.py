from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        #queue = deque(root)
        queue = [root]
        flag = 1
        res = []
        while queue:
            tmp = []
            for i in range(len(queue)):
                #n = queue.popleft()
                n = queue.pop(0)
                tmp.append(n.val)
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
            res.append(tmp[::flag])
            flag*=-1
        return res
if __name__ == '__main__':
    board = [3,9,20,None,None,15,7]
    s = Solution()
    print(s.zigzagLevelOrder(board))