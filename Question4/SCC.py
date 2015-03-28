'''
Created on Apr 8, 2014

The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph. 

@author: J.Wang
'''

import sys
import threading

def readDirectedGraph(filename):
    f = open(filename)
    
    adjlist = []
    adjlist_reversed = []
    
    for line in f:
        num1, num2 = line.split()
        print num1, num2
        v_from = int(num1)
        v_to = int(num2)
        max_v = max(v_from, v_to)
        
        while len(adjlist) < max_v:
            adjlist.append([])
        while len(adjlist_reversed) < max_v:
            adjlist_reversed.append([])
            
        adjlist[v_from-1].append(v_to-1)
        adjlist_reversed[v_to-1].append(v_from-1)
            
    return adjlist, adjlist_reversed


t = 0
s = None
explored = None
leader = None
scc_size = 0
sorted_by_finish_time = None

def DFS_Loop_1(graph_rev, n):
    
    global t, explored, sorted_by_finish_time
    
    t = 0
    explored = [False]*n
    sorted_by_finish_time = [None]*n
    
    for i in reversed(range(n)):
        if not explored[i]:
            DFS_1(graph_rev, i)
                        
            
def DFS_1(graph_rev, i):
    
    global t, explored
    
    explored[i] = True
    
    for v in graph_rev[i]:
        if not explored[v]:
            DFS_1(graph_rev, v)
    
    sorted_by_finish_time[t] = i
    t += 1
    
    
def DFS_Loop_2(graph):
    
    global scc_size, explored, sorted_by_finish_time
    
    explored = [False]*len(graph)
    res = []
    
    for i in reversed(range(len(graph))):
        if not explored[sorted_by_finish_time[i]]:
            scc_size = 0
            # Here we collect all the members
            # of the next SCC using DFS.
            # scc_size is incremented inside DFS.
            DFS_2(graph, sorted_by_finish_time[i])
            res.append(scc_size)
            
    return res
    
    
def DFS_2(graph, i):
    
    global explored, scc_size
    
    explored[i] = True
    
    for v in graph[i]:
        if not explored[v]:
            DFS_2(graph, v)
    
    scc_size += 1
  

def kosarajuSCCsizes(graph, graph_rev):
    
    DFS_Loop_1(graph_rev, len(graph))
    res = DFS_Loop_2(graph)
    
    return res

def main():
    
    graph, graph_rev = readDirectedGraph('SCC.txt')
    
    res = kosarajuSCCsizes(graph, graph_rev)
    
    print(','.join(map(lambda x: str(x), sorted(res)[::-1][:5])))

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target