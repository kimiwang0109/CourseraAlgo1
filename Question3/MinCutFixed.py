'''
Created on Apr 4, 2014

The file contains the adjacency list representation of a simple undirected graph. There are 40 vertices labeled 1 to 40. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks liks : "6 29 32 37 27 16". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 29, 32, 37, 27 and 16.

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut. 

@author: J.Wang
'''
def main():
    import random
    from collections import OrderedDict
    f = open("kargerMinCut.txt")
    arr = []
    dict = {}
    for line in f:
        tokens = line.split()
        dict[tokens[0]] = tokens[1:]
        for t in tokens[1:]:
            arr.append((tokens[0], t))
    
    #print arr    
    while len(dict) > 2:
        (row, col) = arr.pop(random.randint(0, len(arr)-1))
        
        target = col
        #print row,col
        dict[row] += dict[target]
        dict[row] = [x for x in dict[row] if (x!=target and x!=row)]
                
        for k in dict.keys():
            for i in range(len(dict[k])):
                if dict[k][i] == target:
                    dict[k][i] = row
                    
        del dict[target]
            
        for ind in range(len(arr)):
            if arr[ind][0] == target:
                arr[ind] = (row, arr[ind][1])
            if arr[ind][1] == target:
                arr[ind] = (arr[ind][0], row)
        arr = [a for a in arr if a[0]!=a[1]]
        #print arr
        #print OrderedDict(sorted(dict.items(), key=lambda t: int(t[0])))
        #print "length: ", len(dict)
                
    #print OrderedDict(sorted(dict.items(), key=lambda t: int(t[0])))
    print len(dict[dict.keys()[0]])
    return len(dict[dict.keys()[0]])
    
arr=[]
for i in range(100):
    arr.append(main())
    
print min(arr)