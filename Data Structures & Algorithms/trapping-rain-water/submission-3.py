class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l = len(height)
        lp = 0
        rp = l - 1
        leftMax = height[lp]
        rightMax = height[rp]

        result = 0
        while lp < rp:
            if leftMax <= rightMax:
                lp += 1
                result += max(leftMax - height[lp], 0)
                leftMax = max(leftMax, height[lp])
            else:
                rp -= 1
                result += max(rightMax - height[rp], 0)
                rightMax = max(rightMax, height[rp])

        return result