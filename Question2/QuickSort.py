'''
Created on Apr 4, 2014

The file contains all of the integers between 1 and 10,000 (inclusive) in unsorted order (with no integer repeated). The integer in the ith row of the file gives you the ith entry of an input array.

Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.
You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply add m−1 to your running total of comparisons. (This is because the pivot element will be compared to each of the other m−1 elements in the subarray in this recursive call.)

@author: J.Wang
'''
def getMedian(x):
    return sorted(x)[1]

def Partition(arr, l, r):
    li = [arr[0], arr[(r-1)/2], arr[r-1]]
    pilot = getMedian(li)     
    #pilot = arr[r-1]
    m = arr.index(pilot)
    arr[l], arr[m] = arr[m], arr[l]
    i = l+1
    for j in range(l+1, r):
        if arr[j] < pilot:
            arr[j], arr[i] = arr[i], arr[j]
            i +=1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1
    
def QuickSort(arr, comp):
    n = len(arr)
    if n == 1 or n==0:
        return arr, comp
    loc = Partition(arr, 0, n)
    comp += n-1
    left, comp1 = QuickSort(arr[:loc], comp)
    right, comp2 = QuickSort(arr[loc+1:], comp1)
    return left +[arr[loc]]+ right, comp2

print QuickSort([4,3,2,1],0)

#print QuickSort([1,3,5,2,4,6],0)

f = open("QuickSort.txt")
arr = []
for line in f:
    arr.append(int(line))
    
print QuickSort(arr,0)[1]