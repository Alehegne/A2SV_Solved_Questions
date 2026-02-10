class Solution:
    def isHappy(self, n: int) -> bool:
        def getDigitSquare(num):
            sum_ = 0
            while num>0:
                dig = num%10
                sum_=sum_+dig**2
                num = num//10
            return sum_


        vis = set()
        while n not in vis:
            vis.add(n)
            square = getDigitSquare(n)
            if square == 1:
                return True
            n= square
        else:
            return False
