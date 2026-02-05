#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        #Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].
        a_f = Counter(a)
        for e in b:
            if e not in a_f:
                return False
            else:
                a_f[e]-=1
                if a_f[e]==0:
                    del a_f[e]
        return True
    
    
    
    
