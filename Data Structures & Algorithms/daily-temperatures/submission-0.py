class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = len(temperatures) * [0]

        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index

            stack.append((temperatures[i],i))
        return res