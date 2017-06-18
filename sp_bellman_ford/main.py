import os
from common.graph import create_graph_from_file
from sp_bellman_ford.bellman_ford import BellmanFordSP


def main(argv):
    file, s = argv
    g = create_graph_from_file(os.getcwd() + "/" + file)
    d = BellmanFordSP(g, s)

    print("Distance to 9: {} from {}".format(d.dist_to(9), s))
    print("Path to 9: {}  from {}".format(d.path_to(9), s))

if __name__ == "__main__":

    main(("10.txt", 2))
