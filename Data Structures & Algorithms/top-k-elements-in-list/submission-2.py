from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         sorted_counter = Counter(nums).most_common(k)
         return [k for k, v in sorted_counter]