from stack import ArrayStack

# Solution1
# class MinStack(ArrayStack):
#     def __init__(self):
#         super().__init__()
# # 记录栈顶和最小值的差
#         self._min = None

#     def push(self, e):
#         if self.is_empty():
#             self._min = e
#             super().push(0)
#         else:
#             delta = e - self._min
#             super().push(e - self._min)
#             if delta < 0:
#                 self._min = e

#     def pop(self):
#         answer = super().pop()
# #最小值发生变化 说明push为min,之前的min为min+answer
#         if answer < 0:
#             tmp = self._min
#             self._min = self._min - answer
#             return tmp
#         else:
#             return self._min + answer
#     def top(self):
#         answer = super().pop()
#         if answer<0:
#             return self._min
#         else:
#             return self._min + answer
#     def getMin(self):
#         return self._min

# Solution2
class MinStack:
    def __init__(self):
        self._stack = ArrayStack()
        self._minStack = ArrayStack()

    def push(self, e):
        self._stack.push(e)
        if self._minStack.is_empty() or self._minStack.top() > e:
            self._minStack.push(e)

    def pop(self):
        answer = self._stack.pop()
        if answer == self._minStack.top():
            self._minStack.pop()
        return answer

    def getMin(self):
        return self._minStack.top()

    def top(self):
        return self._stack.top()


if __name__ == "__main__":
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
