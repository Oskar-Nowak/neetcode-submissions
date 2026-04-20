class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        lp = 0
        rp = l - 1
        max_area = 0
        while lp < rp:
            area = min(heights[lp], heights[rp]) * (rp - lp)
            max_area = max(area, max_area)
            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
        return max_area
            