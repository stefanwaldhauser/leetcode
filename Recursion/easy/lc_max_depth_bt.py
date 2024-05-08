# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        return max(left_max_depth, right_max_depth) + 1


# Time complexity: we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes.
# Space complexity: in the worst case, the tree is completely unbalanced, e.g. each node has only left child node, the recursion call would occur
# N times (the height of the tree), therefore the storage to keep the call stack would be O(N).
# But in the best case (the tree is completely balanced), the height of the tree would be log⁡(N).
# Therefore, the space complexity in this case would be O(log⁡(N).
