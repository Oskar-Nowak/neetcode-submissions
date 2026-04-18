class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if target - nums[i] in d:
                return sorted([i, d[target - nums[i]]])
            else:
                d[nums[i]] = i