class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pushed_index = 0
        popped_index = 0
        while pushed_index < len(pushed) and popped_index < len(popped):
            stack.append(pushed[pushed_index])
            pushed_index += 1
            while len(stack) > 0 and stack[-1] == popped[popped_index]:
                popped_index += 1
                stack.pop()
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution.validateStackSequences(Solution(), [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))

