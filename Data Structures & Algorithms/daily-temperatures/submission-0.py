class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result: list = [0] * length
        stack: list[tuple] = []

        for i in range(length): 
            while stack and stack[-1][0] < temperatures[i]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append((temperatures[i], i))

        return result
