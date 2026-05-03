class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if stack and stack[-1] >= time:
                continue

            stack.append(time)

        return len(stack)