class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            t = temperatures[i]

            while stk and t > temperatures[stk[-1]]:
                prev = stk.pop()
                output[prev] = i - prev

            stk.append(i) 

        return output