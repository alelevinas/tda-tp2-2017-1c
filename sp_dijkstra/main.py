import os
from common.graph import create_graph_from_file
from sp_dijkstra.dijkstra import DijkstraSP


def main(argv):
    file, s = argv
    g = create_graph_from_file(os.getcwd() + "/" + file)
    d = DijkstraSP(g, s)

    print("Distance to 9: {} from {}".format(d.dist_to(9), s))
    print("Path to 9: {}  from {}".format(d.path_to(9), s))


if __name__ == "__main__":

    main(("10.txt", 2))
