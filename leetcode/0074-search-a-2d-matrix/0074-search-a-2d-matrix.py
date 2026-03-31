class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        flatten = [el for row in matrix for el in row]
        
        def bins(l,r):
            nonlocal flatten

            mid = (l + r)//2
            if flatten[mid] == target:
                return True
            
            if l > r:
                return False
            
            if flatten[mid] > target:
                return bins(l,mid-1)
            else:
                return bins(mid+1,r)


        return bins(0,len(flatten)-1)


        