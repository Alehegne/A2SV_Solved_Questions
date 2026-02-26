import sys
input = sys.stdin.readline
from collections import Counter
def solve():
    n,m = map(int,input().split())
    a,b= list(list(map(int,input().split())) for _ in range(2))
    ca = Counter(a)
    cb = Counter(b)
    c = 0
    for k in ca:
        if k in cb:
            c += ca[k] * cb[k]
    print(c)

    
solve()

