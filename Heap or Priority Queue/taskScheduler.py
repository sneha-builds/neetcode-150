# Task Scheduler

"""
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z.
You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Constraints:

  . 1 <= tasks.length <= 1000
  . 0<= n <= 100

"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26

        for task in tasks:
            count[ord(task) - ord('A')] +=1

        maxf = max(count)
        maxCount=0

        for i in count:
            maxCount +=1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)
        