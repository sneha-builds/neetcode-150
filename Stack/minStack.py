"""Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O(1) time.

"""

class MinStack:

    def __init__(self):
        self.stack =[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        temp=[]
        minimum=self.stack[-1]
        while len(self.stack):
            minimum= min(minimum, self.stack[-1])
            temp.append(self.stack.pop())

        while len(temp):
            self.stack.append(temp.pop())

        return minimum