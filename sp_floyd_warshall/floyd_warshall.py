INF = float("inf")
class FloydWarshallSP:
    def __init__(self, g, s):
        '''
        Calcula las el camino minimo para todos los vertices del grafo.
        :param g: grafo implementando la interfaz de la clase Digraph
        '''
        self.g = g
        self.s = s
        # nextTo[u,v] = x para ir de u a v el proximo nodo desde u es x
        self.nextTo = [[None for _ in range(g.V())] for _ in range(g.V())]
        # FloydWarshal matrix fw[u][v] = SP(u,v) (weight)
        self.fw = [[INF if u != v else 0 for u in range(g.V())] for v in range(g.V())]

        self.create_fw_matrix()

    def create_fw_matrix(self):
        '''
        Executes the Floyd-Warshall algorithm for Smallest Path between all nodes
        :return:
        '''
        # initial weights
        for e in self.g.iter_edges():
            self.fw[e.src][e.dst] = e.weight
            self.nextTo[e.src][e.dst] = e.dst

        # fw alg
        for k in range(self.g.V()):
            for i in range(self.g.V()):
                for j in range(self.g.V()):
                    if self.fw[i][j] > self.fw[i][k] + self.fw[k][j]:
                        self.fw[i][j] = self.fw[i][k] + self.fw[k][j]
                        self.nextTo[i][j] = self.nextTo[i][k]

    def dist_to(self, v):
        return self.fw[self.s][v]

    def path_to(self, v):
        u = self.s
        if self.nextTo[u][v] is None:
            return []
        path = [u]
        while u != v:
            u = self.nextTo[u][v]
            path.append(u)

        return path
