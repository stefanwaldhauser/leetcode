# https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=problem-list-v2&envId=binary-search


# Given a complete binary tree
#
# Every level, except possibly the last, is completely filled in a complete binary tree
# and all nodes in the last level are as far left as possible. It can have between 1 and 2**h nodes inclusive at the last level h.


# Can we do it without iterating over each node in the tree (better than O(N))
# To get the number of nodes we need to find
# the height h of the tree
# Height is not enough as I need to know if the last level is full or not


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_height(self, root):
        """
        Calculate the 0-indexed height of a binary tree.

        The height is defined as the number of edges on the longest path
        from the root to a leaf.

        An empty tree has a height of -1.
        A root tree has a height of 0.

        Args:
        root: The root node of the binary tree.

        Returns:
        int: The height of the tree.
        """
        if root is None:
            return -1

        height = -1
        current_node = root

        while current_node is not None:
            height += 1
            current_node = current_node.left # Works because complete binary trees are left leaning!

        return height



    def find_path(self, target_height, target_position):
        """
        Determines the path from root to the target node in a perfect binary tree.

        Args:
        target_height (int): The height of the target node (0-indexed).
        target_position (int): The position of the target node at its height (0-indexed).

        Returns:
        list: A list of 'L' and 'R' indicating left and right moves to reach the target from the root.
        """
        path = []

        while target_height > 0:
            if target_position % 2 == 0:
                # If position is even, we are the left child of our parent
                # This is because in a perfect binary tree, even positions are left children
                path.append('L')
                target_position //= 2  # Move to parent (integer division)
                                    # For even positions, dividing by 2 gives the parent's position
            else:
                # If position is odd, we are the right child of our parent
                # This is because in a perfect binary tree, odd positions are right children
                path.append('R')
                target_position = (target_position - 1) // 2  # Move to parent
                                                            # For odd positions, we first subtract 1 to get to the left sibling,
                                                            # then divide by 2 to get the parent's position
            target_height -= 1  # Move up one level in the tree

        # We created the path from the target-to-root direction,
        # so now we need to reverse it to get the root-to-target direction
        return path[::-1]  # Reverse the path using slice notation



    def traverse_path(self, root, path):
        """
        Traverses the binary tree along a given path to find a target node.

        This function follows a sequence of left and right moves from the root
        to locate a specific node in the binary tree.

        Args:
        root: The root node of the binary tree.
        path: A list of 'L' and 'R' indicating left and right moves to reach the target from the root.

        Returns:
        Node: The target node if found, None otherwise.
        """
        current_node = root

        for direction in path:
            if current_node is None:
                # If we hit a None node before finishing the path, the target doesn't exist
                return None

            if direction == 'L':
                current_node = current_node.left
            elif direction == 'R':
                current_node = current_node.right
            else:
                # If we encounter an invalid direction, we should return None
                return None
        # At this point, we've either found our target node or reached the end of the path
        return current_node


    def count_inner_level_nodes(self, root, height):
        """
        Counts the number of nodes in all levels except the last one in a perfect binary tree.

        In a perfect binary tree, every level except possibly the last is completely filled.
        This function calculates the sum of nodes in all these completely filled levels.

        Args:
        root: The root node of the binary tree (not used in this implementation but kept for consistency).
        height: The total height of the tree (0-indexed).

        Returns:
        int: The total number of nodes in all levels except the last one.
        """
        inner_height = height - 1
        total_inner_nodes = 0

        while inner_height >= 0:
            # At each level, the number of nodes is 2^level
            nodes_at_level = 2 ** inner_height
            total_inner_nodes += nodes_at_level
            inner_height -= 1

        return total_inner_nodes


    def count_last_level_nodes(self, root: TreeNode, height: int) -> int:
        """
        Counts the number of nodes in the last level of a complete binary tree.

        This function uses binary search to find the rightmost node in the last level,
        which effectively gives us the count of nodes in that level.

        Args:
        root (TreeNode): The root node of the binary tree.
        height (int): The height of the tree (0-indexed).

        Returns:
        int: The number of nodes in the last level of the tree.
        """
        # The possible positions in the last level are [0, (2**height)-1]
        left = 0
        right = (2 ** height) - 1

        def node_exists(position):
            """Check if a node exists at the given position in the last level."""
            path = self.find_path(height, position)
            node = self.traverse_path(root, path)
            return node is not None

        while left < right:
            mid = left + (right - left + 1) // 2

            if node_exists(mid):
                # Node at position mid exists, which means all lower positions also exist but there could be higher existing positions
                left = mid
            else:
                # Node at position mid does not exist, which means all higher positions also do not exists
                right = mid - 1

        # The number of nodes is one more than the maximum position that exists in the last level
        return right + 1


    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        h = self.get_height(root)
        if h == 0:
            return 1
        nodes_inner_levels = self.count_inner_level_nodes(root, h)
        nodes_last_level = self.count_last_level_nodes(root, h)
        return nodes_inner_levels + nodes_last_level
