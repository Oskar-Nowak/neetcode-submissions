# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth: int = 1

        stack = [(root, 1)]

        max_depth = 1

        while stack:
            node, current_depth = stack.pop()

            max_depth = max(max_depth, current_depth)

            if node.left:
                stack.append((node.left, current_depth + 1))

            if node.right:
                stack.append((node.right, current_depth + 1))

        return max_depth

