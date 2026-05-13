class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # tasks.sort()

        tasks = sorted((start,length,idx) for idx,(start,length) in enumerate(tasks))
        #tasks:-  start,process,idx
        idx = 0
        n = len(tasks)
        ans = []
        min_heap = [(tasks[0][1],tasks[0][2],tasks[0][0])] #process time, idx,start time
        time = 0

        # print("tasks:",tasks,"min_heap:",min_heap)
        while min_heap:

            length,curr_idx,start= heapq.heappop(min_heap)
            if time < start:
                time = start + length
            else:
                time += length
            ans.append(curr_idx)
            
            while idx + 1< n and tasks[idx+1][0] <= time:
                idx += 1
                heapq.heappush(min_heap,(tasks[idx][1],tasks[idx][2],tasks[idx][0]))
            if not min_heap and idx + 1 < n:
                idx += 1
                heapq.heappush(min_heap,(tasks[idx][1],tasks[idx][2],tasks[idx][0]))
            # print("min_heap:",min_heap,"ans:",ans)
        return ans
