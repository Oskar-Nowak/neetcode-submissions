class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_sequence = 0
        for num in hashset:
            if num - 1 not in hashset:
                tmp_num = num
                tmp_len = 0
                while tmp_num in hashset:
                    tmp_len += 1
                    tmp_num += 1
                longest_sequence = max(longest_sequence, tmp_len)
        return longest_sequence
