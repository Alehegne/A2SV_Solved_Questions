class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:


        r = len(img)
        c = len(img[0])
        ans = [[0]*c for _ in range(r)]

        for i in range(r):
            for j in range(c):

                sum_ = img[i][j]
                cnt = 1
                #right
                if j + 1<c:
                    sum_ += img[i][j+1]
                    cnt+=1
                #down
                if i + 1<r:
                    sum_ += img[i+1][j]
                    cnt+=1
                #left
                if j - 1 >= 0:
                    sum_ += img[i][j-1]
                    cnt+=1
                #top
                if i-1 >=0:
                    sum_ += img[i-1][j]
                    cnt+=1
                #top-right
                if i-1 >= 0 and j + 1<c:
                    sum_ += img[i-1][j+1]
                    cnt+=1
                #top-left
                if i-1 >=0 and j-1>=0:
                    sum_ += img[i-1][j-1]
                    cnt+=1
                #bottom-left
                if i + 1<r and j - 1 >=0:
                    sum_ += img[i+1][j-1]
                    cnt+=1
                #bottom-right
                if i+ 1 < r and j + 1 < c:
                    sum_ += img[i+1][j+1]
                    cnt+=1
                ans[i][j] = sum_//cnt
        return ans

        
