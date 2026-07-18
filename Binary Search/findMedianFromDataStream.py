# Find median from data stream

"""
The median is the median value in a sorted list of integers. For lists of even length, there is no middle values, so the median is the 
mean of the two middle values.

For example:
  . For arr = [1,2,3], the median is 2
  . For arr = [1,2], the median is (1+2) /2 = 1.5

Implement the MedianFinder class:
  . MedianFinder() initialises the MedianFinder object.
  . void addNum(int num) adds the integer num from the data stream to the data structure.
  . double findMedian() return the median of all elements so far.

Constraints:
  . -100,000 <= num <= 100,000
  . findMedian will only be called after adding at least one integer to the data structure.
"""


class MedianFinder:

    def __init__(self):
        self.data= []        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        return (self.data[n //2] if (n & 1) else
        (self.data[n // 2] + self.data[n // 2-1])/ 2)
        
        