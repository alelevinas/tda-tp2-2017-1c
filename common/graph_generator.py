import random
from random import sample

random.seed()

MIN_V = 5
MAX_V = 500
FILE_NAME = "assign-tmp"

def generate_complete_digraph(n, file_name = FILE_NAME):
    print(n)
    with open(file_name + ".txt", "w") as f:
        f.write(str(n) + "\n")                                      # Vertices
        f.write(str(n * (n-1)))
        f.write("\n")# Edges
        [f.write("{} {} {}\n".format(a, b, round(random.uniform(0.001, 1.000), 3))) for a in range(n) for b in range(n) if a != b]


def main(argv):
    generate_complete_digraph(int(argv[0]), argv[1])

if __name__ == "__main__":
    import sys
    main(sys.argv)

'''
FORMATO DE GRAFO
10 # N°vertices
20 # N°edges
1 0 0.12 #start end weight
5 4 0.90
7 6 0.79
0 1 0.46
6 7 0.12
1 3 0.76
3 6 0.46
0 4 0.23
4 8 0.367
0 5 0.35
4 9 0.3
0 6 0.67
2 8 0.456
0 9 0.345
9 0 0.123
9 1 0.98
8 2 0.76
5 0 0.36
7 3 0.35
6 3 0.4
'''
