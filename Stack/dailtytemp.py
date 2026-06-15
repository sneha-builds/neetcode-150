#Stack : Daily Temperature

"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        num = len(temperatures)
        result = []

        for i in range(num):
            count = 1
            j = i + 1
            while j < num:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == num else count
            result.append(count)
        return result