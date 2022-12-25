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

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            day_pass = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temp:
                    ans[i] = day_pass + 1
                    break
                else:
                    day_pass += 1           
        return ans
