class MedianFinder:

    def __init__(self):
        self.mx_heap = [] #for left less elements
        self.mn_heap = [] #for right greater elements
        
    def addNum(self, num: int) -> None:

        heapq.heappush(self.mx_heap,-num)
        #order 
        if self.mn_heap and -self.mx_heap[0] > self.mn_heap[0]:
            heapq.heappush(self.mn_heap,-heapq.heappop(self.mx_heap))
        
        #size
        if len(self.mx_heap) > len(self.mn_heap)+1:
            heapq.heappush(self.mn_heap,-heapq.heappop(self.mx_heap))
        elif len(self.mn_heap) > len(self.mx_heap):
            heapq.heappush(self.mx_heap,-heapq.heappop(self.mn_heap))

    def findMedian(self) -> float:
        # print("mx:",self.mx_heap,self.mn_heap)
        if len(self.mx_heap) > len(self.mn_heap):
            return -self.mx_heap[0]
        else:
            return (-self.mx_heap[0] + self.mn_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
