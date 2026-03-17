class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7
  
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n == 1:
                return x
            if n % 2 != 0:
                return x*pow((x*x)%self.MOD,(n-1)//2)
            else:
                return pow((x*x)%self.MOD,n//2)
        return pow(x,n)
    def countGoodNumbers(self, n: int) -> int:
        # MOD = self.myPow(10,9) + 7
        
        if n == 1:
            return 5
        isEven = True if n % 2 == 0 else False
        five = n//2 if isEven else n//2 + 1
        four = n//2
        return (self.myPow(5,five) % self.MOD * self.myPow(4,four) % self.MOD) % self.MOD
        
