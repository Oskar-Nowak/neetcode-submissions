from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)  # O(n)

        freq = [[] for _ in range (len(nums) + 1)]  # O(n)

        for num, cnt in counter.items():
            freq[cnt].append(num)  # O(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res

