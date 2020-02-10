
class Graph:

    class Vertex:
        __slots__ = '_element'

        def __init__(self, x):
            self._element = x

        def element(self):
            return self._element

        def __hash__(self,):
            return hash(id(self))

    class Edge:
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return self._origin, self._destination

        def opposite(self, u):
            return self._destination if u is self._origin else self._origin

        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))
    def __init__(self,directed):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing.keys())
        return total if self.is_directed() else total//2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values:
            yield edge

    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        edge = self.Edge(u, v, x)
        self._outgoing[u][v] = edge
        self._incoming[v][u] = edge
    def remove_vertex(self,v):
        if not v in self._outgoing:
            raise ValueError('v is not in the graph')
        else:
            adj = self._outgoing.pop(v)
            for u in adj:
                del self._incoming[u][v]
            if self.is_directed():
                adj = self._incoming.pop(v)
                for u in adj:
                    del self._outgoing[u][v]
        return v.element()

    def remove_edge(self,e):
        u,v = e.endpoints()
        del self._outgoing[u][v]
        del self._incoming[v][u]
        return e.element()

def DFS(g,u,discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g,v,discovered)
def construct_path(u,v,discovered):
    '''u is the specific start vertex of the DFS''' 
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[v]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path


