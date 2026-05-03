class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for i in range(len(cars)):
            if stack and(target - stack[-1][0]) / stack[-1][1] >= (target - cars[i][0]) / cars[i][1]:
                continue
            else:
                stack.append(cars[i])

        return len(stack)