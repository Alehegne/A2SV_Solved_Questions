class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:



        # for im in image:
        #     im.reverse()
        # n = len(image)
        # m = len(image[0])

        # for i in range(n):
        #     for j in range(m):
        #         image[i][j] = 0 if image[i][j] == 1 else 1
        # return image
        return [list(0 if i==1 else 1 for i in reversed(im)) for im in image]
        
