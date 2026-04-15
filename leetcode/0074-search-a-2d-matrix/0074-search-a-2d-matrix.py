class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        def get_row():
            l,r = 0,len(matrix)-1
            ans = 0
            while l <= r:
                mid = (l + r)//2
                if target < matrix[mid][0]:
                    r = mid - 1
                else:
                    ans = mid
                    l = mid + 1
            return ans
        def get_ele(row):
            l,r = 0,len(matrix[row])-1
            while l <= r:
                mid = (l+r)//2
                if target == matrix[row][mid]:
                    return True
                elif target > matrix[row][mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        row = get_row()
        print("row:",row)
        return get_ele(row)


        