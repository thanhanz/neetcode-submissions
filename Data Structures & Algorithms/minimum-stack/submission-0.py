class MinStack:
    # When append numbers into minStack, I have to store the in during that (using 2D array)
    # One is position (normal stack) and second is the min value when insert that

    # push(5) -> (5, 5)
    # push(2) -> (2, 2)
    # push(7) -> (7, 2)
    # push(1) -> (1, 1)
    # push(9) -> (9, 1)

    # Push a pair ([0][1]) with [0] is real value and [1] is the current_min of that


    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
