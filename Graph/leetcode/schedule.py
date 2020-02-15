class Solution(object):
    class Node:
        def __init__(self, val, incoming_degree=0, outcoming=[]):
            self.val = val
            self.incoming_degree = incoming_degree
            self.outcoming = outcoming

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        classes = [self.Node(i, 0, []) for i in range(numCourses)]
        for u, v in prerequisites:
            classes[u].incoming_degree += 1
            classes[v].outcoming.append(classes[u])

        def find_no_incoming_degree(classes):
            for index in range(len(classes)):
                u = classes[index]
                if u.incoming_degree == 0:
                    return index
            return -1
        walk = find_no_incoming_degree(classes)
        while walk != -1:
            for v in classes[walk].outcoming:
                v.incoming_degree -= 1
            classes.pop(walk)
            walk = find_no_incoming_degree(classes)
        return len(classes) == 0


if __name__ == "__main__":
    print(Solution().canFinish(3, [[1, 0], [2, 0]]))
