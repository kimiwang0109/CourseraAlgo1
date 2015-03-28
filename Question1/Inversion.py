'''
Created on Apr 4, 2014

The file contains all the 100,000 integers between 1 and 100,000 (including both) in some random order( no integer is repeated).

Your task is to find the number of inversions in the file given (every row has a single integer between 1 and 100,000). Assume your array is from 1 to 100,000 and ith row of the file gives you the ith entry of the array.
Write a program and run over the file given. The numeric answer should be written in the space.

@author: J.Wang
'''
def Merge_and_CountSplitInv(s1, s2):
    i,j = 0,0
    li = []
    m = 0
    while i<len(s1) and j<len(s2):
        if s1[i] < s2[j]:
            li.append(s1[i])
            i+=1
        elif s2[j] < s1[i]:
            li.append(s2[j])
            j+=1
            m+=len(s1)-i
    if i == len(s1):
        li += s2[j:]
    elif j == len(s2):
        li += s1[i:]
    return li, m
    
    
def Sort_and_Count(arr):
    n = len(arr)
    if n==1 or n==0:
        return arr,0
    else:
        s1, x = Sort_and_Count(arr[:n/2])
        s2, y = Sort_and_Count(arr[n/2:])
        s3, z = Merge_and_CountSplitInv(s1, s2)
        return s3, x+y+z
    
    
#print Sort_and_Count([4,3,2,1])
#print Sort_and_Count([1,3,5,2,4,6])
f = open("IntegerArray.txt")
arr = []
for line in f:
    arr.append(int(line))
    
print Sort_and_Count(arr)[1]
