class Solution(object):
    class Node:
        def __init__(self, val, incoming_degree=0, outcoming=[]):
            self.val = val
            self.incoming_degree = incoming_degree
            self.outcoming = outcoming
            self.marked = False
            self.traversd = False

    def findOrder2(self, numCourses, prerequisites):
        classes = [self.Node(i, 0, []) for i in range(numCourses)]
        order = []
        for u, v in prerequisites:
            classes[u].incoming_degree += 1
            classes[v].outcoming.append(classes[u])

        global possible
        possible = True

        def DFS(start, discovered):
            global possible
            if start.traversd:
                return
            start.marked = True
            for v in start.outcoming:
                if v.marked:
                    possible = False
                    return
                elif not v.traversd:
                    DFS(v, discovered)
            start.traversd = True
            start.marked = False
            discovered.append(start.val)

        order = []
        for start in classes:
            DFS(start, order)
            if not possible:
                break
        return order[::-1] if possible else []

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        classes = [self.Node(i, 0, []) for i in range(numCourses)]
        order = []
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
            order.append(classes[walk].val)
            walk = find_no_incoming_degree(classes)
        return order if len(classes) == 0 else []


if __name__ == "__main__":
    print(Solution().findOrder2(2, [[1, 0], [0, 1]]))

