class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        def inbound(r,c):
            return 0<=r<n and 0<=c<m


        ans = [[0]*m for _ in range(n)]
        #direction vectors
        dir_ = [
        (0, 1),   # N
        (1, 1),   # NE
        (1, 0),   # E
        (1, -1),  # SE
        (0, -1),  # S
        (-1, -1), # SW
        (-1, 0),  # W
        (-1, 1)   # NW
    ]


        for r in range(n):
            for c in range(m):

                sum_ = img[r][c]
                cnt = 1
                for d1,d2 in dir_:
                    x = d1+r
                    y = d2+c
                    if inbound(x,y):
                        sum_+=img[x][y]
                        cnt += 1
                ans[r][c] = sum_//cnt
                




                # cnt = 1
                # #right
                # if j + 1<c:
                #     sum_ += img[i][j+1]
                #     cnt+=1
                # #down
                # if i + 1<r:
                #     sum_ += img[i+1][j]
                #     cnt+=1
                # #left
                # if j - 1 >= 0:
                #     sum_ += img[i][j-1]
                #     cnt+=1
                # #top
                # if i-1 >=0:
                #     sum_ += img[i-1][j]
                #     cnt+=1
                # #top-right
                # if i-1 >= 0 and j + 1<c:
                #     sum_ += img[i-1][j+1]
                #     cnt+=1
                # #top-left
                # if i-1 >=0 and j-1>=0:
                #     sum_ += img[i-1][j-1]
                #     cnt+=1
                # #bottom-left
                # if i + 1<r and j - 1 >=0:
                #     sum_ += img[i+1][j-1]
                #     cnt+=1
                # #bottom-right
                # if i+ 1 < r and j + 1 < c:
                #     sum_ += img[i+1][j+1]
                #     cnt+=1
                # ans[i][j] = sum_//cnt
        return ans

        
