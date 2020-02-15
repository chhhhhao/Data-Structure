
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None

        level = [node]
        next_level = []
        cloned = {}
        while len(level)>0:
            for u in level:
                new_node = Node(u.val,[])
                for v in u.neighbors:
                    if v not in cloned:
                        if (v not in next_level) and (v not in level):
                            next_level.append(v)
                        new_node.neighbors.append(v)
                    else:
                        new_node.neighbors.append(cloned[v])
                        i = cloned[v].neighbors.index(u)
                        cloned[v].neighbors[i] = new_node
                cloned[u] = new_node
            level = next_level
            next_level = []
        return cloned[node]








