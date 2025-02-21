'''
Created on Apr 10, 2014

The goal of this problem is to implement a variant of the 2-SUM algorithm (covered in the Week 6 lecture on hash table applications).
The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

@author: J.Wang
'''
f = open("HashInt.txt")
arr = []
dict = {}  # @ReservedAssignment
for line in f:
    l = int(line)
    dict[l] = 1
    arr.append(l)
    
res = 0
for num in range(-10000,10001):
    for t in arr:
        if num-t in dict:
            res+=1
            print num,res
            break
print res