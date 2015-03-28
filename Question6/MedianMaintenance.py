'''
Created on Apr 11, 2014

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 5 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

@author: J.Wang
'''
import heapq
f = open('Median.txt')
heap_low = []
heap_high = []
data = []
for line in f:
    data.append(int(line))
    
res = []

for num in data:
    if len(heap_low) == 0:
        heapq.heappush(heap_low, -num)
    else:
        m = -heap_low[0]
        if num > m:
            heapq.heappush(heap_high, num)
            if len(heap_high) > len(heap_low):
                extract_min = heapq.heappop(heap_high)
                heapq.heappush(heap_low, -extract_min)
        else:
            heapq.heappush(heap_low, -num)
            if len(heap_low) - len(heap_high) > 1:
                extract_max = -heapq.heappop(heap_low)
                heapq.heappush(heap_high, extract_max)
    res.append(-heap_low[0])
    
print sum(res)%10000
                