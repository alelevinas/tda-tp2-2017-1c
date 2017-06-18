import queue
INF = float("inf")
class DijkstraSP:
    def __init__(self, g, s):
        '''
        Calcula las el camino minimo para todos los vertices del grafo g desde el nodo s.
        :param g: grafo implementando la interfaz de la clase Digraph
        '''
        self.g = g
        self.edgeTo = [None for v in range(g.V())]  # self.degeTo[x]: ultima arista que llega a x en su camino minimo desde s
        self.distTo = [INF for v in range(g.V())]
        self.pq = queue.PriorityQueue()

        self.distTo[s] = 0

        self.pq.put((0, s))

        while not self.pq.empty():
            self.relax(self.pq.get())

    def relax(self, item):
        dist, v = item
        if self.distTo[v] < dist:  # era un elemento desactualizado del heap
            return

        for e in self.g.adj_e(v):
            w = e.dst
            if self.distTo[w] > self.distTo[v] + e.weight:
                self.distTo[w] = self.distTo[v] + e.weight
                self.edgeTo[w] = v
                self.pq.put((self.distTo[w], w))
                # si pq contiene w, actualizar su distancia y prioridad
                # sino, agregar w a pq

    def dist_to(self, v):
        return self.distTo[v]

    def path_to(self, v):
        last = v
        path = [v]
        while self.edgeTo[last]:
            last = self.edgeTo[last]
            path.insert(0, last)
        return path
