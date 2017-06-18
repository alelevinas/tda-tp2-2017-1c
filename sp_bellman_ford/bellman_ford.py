import queue
INF = float("inf")
class BellmanFordSP:
    def __init__(self, g, s):
        '''
        Calcula el camino minimo para todos los vertices del grafo g desde el nodo s.
        :param g: grafo implementando la interfaz de la clase Digraph
        '''
        self.g = g
        self.edgeTo = [None for v in range(g.V())]  # edgeTo[x]: ultima arista que llega a x en su camino minimo desde s
        self.distTo = [INF for v in range(g.V())]
        self.distTo[s] = 0

        for v in range(g.V()):
            for e in g.iter_edges():
                if self.distTo[e.dst] > self.distTo[e.src] + e.weight:
                    self.edgeTo[e.dst] = e.src
                    self.distTo[e.dst] = self.distTo[e.src] + e.weight

        for e in g.iter_edges():
            if self.distTo[e.dst] > self.distTo[e.src] + e.weight:
                self.distTo = [INF for v in range(g.V())]
                print("Existen ciclos negativos! (Belman ford)")
                return
        return

    def dist_to(self, v):
        return self.distTo[v]

    def path_to(self, v):
        last = v
        path = [v]
        while self.edgeTo[last]:
            last = self.edgeTo[last]
            path.insert(0, last)
        return path
