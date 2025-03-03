import heapq
def findKthLargest(nums, k):
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
            
    return heap[0]
print(findKthLargest([1,1,1,2,5], 2))