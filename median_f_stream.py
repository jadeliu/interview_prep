__author__ = 'qiong'

# description:
# http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers

import heapq
import random

def get_median():
    minheap, maxheap = [], []
    heapq.heapify(minheap)
    heapq._heapify_max(maxheap)
    median = 0
    while True:
        val = random.random()
        if minheap==None and maxheap==None:
            heapq.heappush(minheap, val)
            median = val
        elif minheap and maxheap==None:
            heapq._heappushpop_max(maxheap, val)
        elif minheap==None and maxheap:
            heapq.heappush(minheap, maxheap[0])
            heapq.heappop(maxheap)
        else:
            if val<minheap[0]:
                heapq.heappush(minheap, val)
            else:
                heapq._heappushpop_max(maxheap, val)
            if len(minheap)>len(maxheap)+1:
                heapq.heappush(minheap, heapq.heappop(maxheap))
            elif len(minheap)+1<len(maxheap):
                heapq._heappushpop_max(maxheap, heapq.heappop(minheap))
        if minheap or maxheap:
            if len(minheap)==len(maxheap):
                median = (minheap[0]+maxheap[0])/2
            elif len(minheap)>len(maxheap):
                median = minheap[0]
            else:
                median = maxheap[0]
        print median
        
print get_median()