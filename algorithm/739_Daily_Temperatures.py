class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # for tracking which day
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                curr = stack.pop()
                ans[curr] = i - curr
            stack.append(i)
        return ans
