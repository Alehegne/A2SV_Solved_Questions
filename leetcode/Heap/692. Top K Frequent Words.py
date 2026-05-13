class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:


        f = Counter(words)

        min_heap = []
        for key,v in f.items():

            heapq.heappush(min_heap,(-v,key))
        
        return [heapq.heappop(min_heap)[1] for _ in range(k)]
            
