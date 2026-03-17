class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = True if n < 0 else False
        if n == 0:
            return 1

        def pow(x,n):
            if n == 1:
                return x
            if n % 2 != 0:
                return x*pow(x*x,(n-1)//2)
            else:
                return pow(x*x,n//2)
        n = abs(n)
        res = pow(x,n)
        return res if not neg else 1/res
        
