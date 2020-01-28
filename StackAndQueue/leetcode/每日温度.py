class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [None] * len(T)
        i = 0
        while i < len(T):
            if len(stack) == 0:
                stack.append((i, T[i]))
                i += 1
            if T[i] <= stack[-1][1]:
                stack.append((i, T[i]))
                i += 1
            elif T[i] > stack[-1][1]:
                index, _ = stack.pop()
                answer[index] = i - index
        for index, _ in stack:
            answer[index] = 0
        return answer

