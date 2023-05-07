'''
Coursera - Algorithms Specialization, Stanford - Programming Assignment - Course 1 Week 2
Serena Rosignoli, 2023

The file contains the adjacency list representation of a simple undirected graph.
There are 200 vertices labeled 1 to 200.
The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to.
So for example, the 6th6th row looks like : "6	155	56	52	120	......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut.  (HINT: Note that you'll have to figure out an implementation of edge contractions.  Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.  But you should also think about more efficient implementations.)   (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.)  Write your numeric answer in the space provided.  So e.g., if your answer is 5, just type 5 in the space provided.
'''


import math
import random

class UndirectedGraph:

    def __init__(self, vertices):
        self.adj_vertices = []
        while vertices > 0:
            self.adj_vertices.append([])
            vertices -= 1


    def copy(self):
        res = UndirectedGraph(0)
        for l in self.adj_vertices:
            res.adj_vertices.append(l[:])
        return res


    def add_edge(self, i, j):
        # Assuming there will be a
        # call of self.add_edge(j, i)
        self.adj_vertices[i].append(j)

    def n(self):
        return len(self.adj_vertices)


    def merge_karger(self, i, j):

        i_adj = self.adj_vertices[i]
        k = 0
        while k < len(i_adj):
            if i_adj[k] == j:
                i_adj.pop(k)
                k -= 1
            k += 1

        for v in self.adj_vertices[j]:
            if (v != i):
                self.add_edge(i, v)
                v_adj = self.adj_vertices[v]
                # Assuming undirected graph
                k = 0
                l = len(v_adj)
                while k < l:
                    if(v_adj[k] == j):
                        v_adj[k] = i
                        break
                    k += 1

        # Optimization: instead of computing a new graph
        # just swap j-th and (n-1)-th lines 'in-place'
        self.adj_vertices[j] = self.adj_vertices[self.n()-1]
        for v in self.adj_vertices[j]:
            v_adj = self.adj_vertices[v]
            # Assuming undirected graph
            k = 0
            l = len(v_adj)
            while k < l:
                if(v_adj[k] == (self.n()-1)):
                    v_adj[k] = j
                    break
                k += 1
        self.adj_vertices.pop()



def _kargerMinCut(graph, seed):

    # Each time - new seed
    random.seed(seed)

    while graph.n() > 2:
        # Picking random edge
        i = random.randint(0, graph.n()-1)
        adj = graph.adj_vertices[i]
        j = random.choice(adj)

        graph.merge_karger(i, j)

    # Two vertices remain
    return len(graph.adj_vertices[0])


def kargerMinCut(graph, N):
    '''
    Computes the minimum cut of the graph.

    Running time lower bound is Omega(N * m), where
    N - number of iterations,
    m - number of graph edges.

    For high success probability (1/n failure chance),
    use N = n^2 * log(n).
    '''

    i = 0

    # (!) Working with the copy of the graph,
    # not destroying the original one
    min_res = _kargerMinCut(graph.copy(), i)
    while i < N:
        t = _kargerMinCut(graph.copy(), i)
        print(str(i)+': '+str(t))
        if t < min_res: min_res = t
        i += 1

    return min_res


def main():

    f = open('kargerMinCut.txt')
    # (!) Even better approach to reading line than in PA2
    lines = f.read().splitlines()
    f.close()

    graph = UndirectedGraph(200)

    for line in lines:
        lst = line.split('\t')
        t = int(lst[0])-1
        for i in lst[1:-1]:
            v = int(i)-1
            graph.add_edge(t, v)

    # To get (1/n) failure probability,
    # repeat the basic procedure n^2 * log(n) times

    N = math.log(graph.n()) #graph.n()**2 * math.log(graph.n())
    print(N)
    for i in range(5):
        print(kargerMinCut(graph, i))


if __name__ == '__main__':
    main()
