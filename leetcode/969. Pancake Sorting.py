class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # v_i = {}
        # for i,v in enumerate(arr):
        #     v_i[v] = i
        def reverse(start,end):
            while start < end:
                arr[start],arr[end] = arr[end],arr[start]
                # v_i[arr[start]] = end
                # v_i[arr[end]] = start
                end -= 1
                start += 1

        initial = 1
        ans = []
        for i in range(len(arr)):
            if initial != arr[-initial]:
                #reverse till initial index
                ans.append(arr.index(initial)+1)
                reverse(0,arr.index(initial))
                #reverse till end endex
                reverse(0,len(arr)-initial)
                ans.append(len(arr) - initial+1)
            initial += 1
        ans.append(len(arr))
        return ans




        
