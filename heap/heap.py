class MinHeap:
    def __init__(self,heap):
        self.heap = heap[:]

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def heapify(self):
        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
            
    def _sift_down(self, *args):
        i = args[0]
        n = args[1] if len(args) > 1 else len(self.heap)
        # print(n)
        min_val = i
        left = self.left_child(min_val)
        right = self.right_child(min_val)
        
        if left < n and self.heap[left] < self.heap[min_val]:
            min_val = left
            
        if right < n and self.heap[right] < self.heap[min_val]:
            min_val = right
        
        if i != min_val:
            self.swap(i, min_val)
            self._sift_down(min_val, n)

    def push(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        
    def peak(self):
        return self.heap[0]
    
    def heappop(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val
    
    def heapsort(self,):
        n = len(self.heap)
        self.heapify()
        for i in range(n-1, 0, -1):
            self.swap(0, i)
            self._sift_down(0, i)
        # return self.heap
        
    def klargest(self, k ):
        
        res = []
        for i in range(k):
            res.append(self.heappop())
        return res
        
    
heap = MinHeap([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
heap.heapify()
res = heap.klargest(3)
print(res)


heap.heapsort()
print(heap.heap)


class MaxHeap:
    def __init__(self, heap):
        self.heap = heap
        self.size = len(heap)
        
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return i * 2 + 1
    
    def right_child(self, i):
        return i * 2 + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def _sift_up(self, i):
        parent = self.parent(i)
        
        if i > 0 and self.heap[parent] > self.heap[i]:
            self.swap(i, parent)
            self._sift_up(parent)
    
    def heappush(self, e):
        self.heap.append(e)
        self.size += 1
        self._sift_up(self.size - 1)
    
        
    def _sift_down(self, i, n):
        left = self.left_child(i)
        right = self.right_child(i)
        max_child = i
        
        if left < n and self.heap[max_child] < self.heap[left]:
            max_child = left
            
        if right < n and self.heap[max_child] < self.heap[right]:
            max_child = right
            
        if i != max_child:
            self.swap(i, max_child)
            self._sift_down(max_child, n)
    
    def peak(self):
        return self.heap[0]
    
    def heappop(self):
        if not self.heap:
            return None 
        
        if self.size == 1:
            return self.heap[0]
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self._sift_down(0, self.size)
        return min_val
    
    def non_leaf_starts(self, n):
        return n // 2 - 1
    
    
    def heapify(self,):
        n = self.size
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i, n)

    def heapsort(self,):
        n = self.size
        self.heapify()
        for i in range(n-1, 0, -1):
            self.swap(0, i)
            self._sift_down(0, i)
        # return self.heap
    
heap = MaxHeap([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# heap.heapsort()
# print(heap.heap)

heap.heapify()
for i in range(5):
    res = heap.heappop()
    print(res)
    
    


    