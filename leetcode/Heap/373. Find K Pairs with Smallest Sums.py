class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:


        #brute force
        min_heap = []

        for i in range(len(nums1)):
            heapq.heappush(min_heap,(nums1[i] + nums2[0],i,0))
        
        print(min_heap)

        mins = []
        for i in range(k):
            sm,idx1,idx2 = heapq.heappop(min_heap)

            mins.append([nums1[idx1],nums2[idx2]])

            if idx2 + 1 < len(nums2):
                heapq.heappush(min_heap,(nums1[idx1] + nums2[idx2+1],idx1,idx2 + 1))
            
            if len(mins) == k:
                break

        return mins

        
