class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] # of touples (height, start_index)
        max_area = 0

        for i in range(n):
            start_index = i
            while stack and stack[-1][0] > heights[i]:
                max_area = max(max_area, stack[-1][0] * (i - stack[-1][1]))
                start_index = stack[-1][1]
                stack.pop()
            stack.append((heights[i], start_index))

        for height, start_index in stack:
            max_area = max(max_area, height * (n - start_index))

        return max_area