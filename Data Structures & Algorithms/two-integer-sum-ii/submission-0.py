class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        lp = 0
        rp = l - 1

        while lp < rp:
            current_sum = numbers[lp] + numbers[rp]
            if current_sum == target:
                return [lp + 1, rp + 1]
            elif current_sum < target:
                lp += 1
            else:
                rp -= 1
        