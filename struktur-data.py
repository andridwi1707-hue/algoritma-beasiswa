class MaxHeapPriorityQueue:
    """Struktur Data 2: Max-Heap untuk Priority Queue[cite: 16, 47]."""
    def __init__(self): 
        self.heap = []
        
    def insert(self, mhs):
        self.heap.append(mhs)
        self._heapify_up(len(self.heap) - 1)
        
    def extract_max(self):
        if not self.heap: 
            return None
        if len(self.heap) == 1: 
            return self.heap.pop()
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_item
        
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index]["skor_akhir"] > self.heap[parent]["skor_akhir"]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
            
    def _heapify_down(self, index):
        left, right, largest = 2*index + 1, 2*index + 2, index
        if left < len(self.heap) and self.heap[left]["skor_akhir"] > self.heap[largest]["skor_akhir"]: 
            largest = left
        if right < len(self.heap) and self.heap[right]["skor_akhir"] > self.heap[largest]["skor_akhir"]: 
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)