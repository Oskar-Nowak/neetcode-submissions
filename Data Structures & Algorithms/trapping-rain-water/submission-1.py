class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = len(height)

        maxLeft = [0] * l
        maxRight = [0] * l

        currentMaxLeft = 0
        for i in range(l):
            maxLeft[i] = currentMaxLeft
            currentMaxLeft = max(currentMaxLeft, height[i])
        
        currentMaxRight = 0
        for i in range(l - 1, -1, -1):
            maxRight[i] = currentMaxRight
            currentMaxRight = max(currentMaxRight, height[i])

        result = 0
        for i in range(l):
            result += max(min(maxLeft[i], maxRight[i]) - height[i], 0)

        return result