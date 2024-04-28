import networkx as nx
import matplotlib.pyplot as plt
import random

def p_function(p):
    return random.random() < p

def CreateRing(N, k):
    G = nx.Graph()
    for i in range(0, N):
        G.add_node(i) 

    K=k//2    
    for i in range(0, N):
        for j in range(i + 1,i + K + 1):
            G.add_edge(i,j%N)
    if(k%2 == 0): return G

    for node in range(0, N):
        if(G.degree[node] < k):
            add_special_edge(G, N, node, False)
    return G


def add_special_edge(G, N, i, rand):
    if(rand):start = random.randint(0, N-1)
    else: start = i
    for j in range(start, N + start):
        j = j%N
        if(j != i and (not G.has_edge(i,j))):
            G.add_edge(i,j)
            return G


def SmallWorldCreat(N, K, p):
    if(p > 1 or p < 0 or K> N or N < 0 or K < 0): return -1
    #Ring creation 
    G = CreateRing(N, K)
    edges = G.edges
    for edge in edges:
        if(p_function(p)):
            n1 = edge[0]
            n2 = edge[1]
            G.remove_edge(n1,n2)
            G = add_special_edge(G, N, n1,True)
    return G

def SmallWorldCheck(G, N, p):
    H = nx.Graph()
    H = nx.erdos_renyi_graph(N,p,123,False)
    C = nx.average_clustering(G)
    Cr = nx.average_clustering(H)
    L = nx.average_shortest_path_length(G)
    Lr = nx.average_shortest_path_length(H)
    s = (C/Cr)/(L/Lr)
    print(s)
    if(s>1):return True
    return False

N = 13
p = 0.8
K = 6
G = nx.watts_strogatz_graph(N, K, p)
SmallWorldCheck(G,N, p)
G = SmallWorldCreat(N, K, p)
SmallWorldCheck(G,N, p)

pos = nx.circular_layout(G)

plt.figure(figsize = (12, 12))
nx.draw_networkx(G,pos)

plt.show()

                


    
        
        
        
