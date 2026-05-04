# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque([(root, 0)])
        output: list[list]= [[]]
        prev_depth = 0

        while queue:
            node, current_depth = queue.popleft()
            
            if current_depth > prev_depth:
                output.append([])
                prev_depth = current_depth
            output[current_depth].append(node.val)

            if node.left:
                queue.append((node.left, current_depth + 1))

            if node.right:
                queue.append((node.right, current_depth + 1))

        return output