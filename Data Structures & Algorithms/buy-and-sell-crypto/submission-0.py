class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)

        if l <= 1:
            return 0
        
        maximumProfit = 0
        lp = 0
        rp = 1

        while rp < l:
            if prices[lp] > prices[rp]:
                lp = rp
                rp += 1
            else:
                maximumProfit = max(maximumProfit, prices[rp] - prices[lp])
                rp += 1
        return maximumProfit