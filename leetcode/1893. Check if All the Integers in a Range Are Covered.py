from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        line=[0]*52

        for start,end in ranges:
            line[start]+=1
            line[end+1]-=1
        #prefix sum
        for i in range(1,len(line)):
            line[i]=line[i-1]+line[i]
        #iterate
        for i in range(left,right+1):
            if line[i]==0:
                return False
        return True


        