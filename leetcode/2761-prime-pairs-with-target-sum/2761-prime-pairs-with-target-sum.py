class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        if n <= 2:
            return []

        def sieve(n):

            prime = [True] * n
            prime[0] = prime[1] = False

            p = 2

            while p * p < n:

                if prime[p]:
                    for j in range(p*p,n,p):
                        prime[j] = False
                p += 1
            return prime
        
        primes = sieve(n)
        ans = []

        for i in range(1,len(primes)//2 + 1):
            if primes[i]:
                if primes[n-i]:
                    ans.append([i,n-i])
        return ans

        