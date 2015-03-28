'''
Created on Apr 10, 2014

In this programming problem you'll code up Dijkstra's shortest-path algorithm. 
Download the text file here. (Right click and save link as). 
The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000. 

@author: J.Wang
'''

f = open("dijkstraData.txt")
dict = {}  # @ReservedAssignment
processed = [1]

for line in f:
    tokens = line.split()
    neighbor = {}
    for t in tokens[1:]:
        tgt, val = t.split(',')
        neighbor[int(tgt)] = int(val)
    dict[int(tokens[0])] = neighbor
    #print len(neighbor)    
#print OrderedDict(sorted(dict.items(), key=lambda t: int(t[0])))
distance = [0]
for i in range(199):
    distance.append(1000000)
    
while len(processed)!= 200:
    edges = []
    for v in processed:
        for edge in dict[v].items():
            if edge[0] not in processed:
                edges.append((v,edge))
    if len(edges) == 747:
        for e in edges:
            print e[0]
    v,(w,dist) = sorted(edges, key=lambda t: t[1][1]+distance[t[0]-1])[0]

    processed.append(w)    
    distance[w-1] = distance[v-1]+dist
    
print distance



li = [7,37,59,82,99,115,133,165,188,197]
for l in li:
    print distance[l-1],