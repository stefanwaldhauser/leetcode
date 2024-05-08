# https://leetcode.com/problems/search-in-a-binary-search-tree/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BST
# left smaller, right bigger

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else: # val >= root.val
            return self.searchBST(root.right, val)


# Time Complexity is O(Height of Tree)
# If the BST is completely unbalanced (only left or only right) the height is N so worst case O(N)
# if it is balanced the height is log2(N) so the average average case is O(log2(N)). Same for the space complexity
