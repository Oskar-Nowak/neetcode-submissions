class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop_max(maxHeap)
            second = heapq.heappop_max(maxHeap)
            if first > second:
                heapq.heappush_max(maxHeap, first - second)

        maxHeap.append(0)
        return maxHeap[0]