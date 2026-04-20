class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result = []
        nums = sorted(nums)
        for i in range(l - 2):
            if i > 0 and nums[i] == prev_i:
                continue
            lp = i + 1
            rp = l - 1
            while lp < rp:
                if nums[lp] + nums[rp] == -1 * nums[i]:
                    result.append([nums[i], nums[lp], nums[rp]])
                    while lp < rp and nums[lp] == nums[lp + 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp - 1]:
                        rp -= 1
                    lp += 1
                    rp -= 1
                elif nums[lp] + nums[rp] > -1 * nums[i]:
                    rp -= 1
                else:
                    lp += 1
            prev_i = nums[i]
        return result
