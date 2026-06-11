"""You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxAr = 0

        for i in range(n):
            height = heights[i]
            rtmt = i+1
            while rtmt < n and heights[rtmt] >= height:
                rtmt += 1

            ltmt = i
            while ltmt >= 0 and heights[ltmt] >= height:
                ltmt -= 1

            rtmt -= 1
            ltmt += 1
            maxAr = max(maxAr, height * (rtmt - ltmt + 1))
        return maxAr

        