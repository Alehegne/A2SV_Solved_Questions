
t=int(input())
from collections import Counter
for _ in range(t):

    n=int(input())
    b=list(map(int,input().split()))
    max_=max(b)
    ops=n
    right=n-b.count(0)-1
    while ops!=max_:
        right-=1
        ops-=1
    print(right+1)



        
      
        






