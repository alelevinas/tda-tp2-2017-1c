import sys
import time

from common.graph_generator import main as gen_main
from sp_bellman_ford.main import main as bf_main
from sp_dijkstra.main import main as dij_main
from sp_floyd_warshall.main import main as fw_main

USAGE = '''
Instrucciones de uso:
        -gen <n> <name>    Genera un digrafo completo de n vértices con todos pesos positivos. Los almacena en el archivo <name>.txt

        -dj <name> <s>     Ejecuta el algoritmo de Dijkstra para encontrar el camino minimo desde s a todos los elementos del grafo <name>
                    
        -bf <name> <s>     Ejecuta el algoritmo de Bellman-Ford para encontrar el camino minimo desde s a todos los elementos del grafo <name>
        
        -fw <name> <s>     Ejecuta el algoritmo Floyd-Warshall para encontrar el camino minimo desde s a todos los elementos del grafo <name>
        '''


def main(argc, argv):
    print("-------TDA TP2-------")
    if argc <= 2:
        print(USAGE)
        return

    print(argv)
    ej, params = argv[1], argv[2:]
    print("hola")
    if ej == "-gen":
        n, file_name = params
        print("Generando Digrafo")
        return measure_time(gen_main, (int(n), file_name))

    if ej == "-dj":
        print(argv)
        file_name, s = params
        print("DIJKSTRA")
        return measure_time(dij_main, (file_name, int(s)))

    if ej == "-bf":
        file_name, s = params
        print("BELLMAN FORD")
        return measure_time(bf_main, (file_name, int(s)))

    if ej == "-fw":
        file_name, s = params
        print("FLOYD WARSHALL")
        return measure_time(fw_main, (file_name, int(s)))


def measure_time(f, n):
    start = time.perf_counter()
    f(n)
    end = time.perf_counter()
    print("Tiempo de ejecución:     {:.5f} segundos".format(end - start))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
