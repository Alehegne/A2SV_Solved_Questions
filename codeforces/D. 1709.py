import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    o = []
    #bubble sort a and b
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                o.append([1,j+1])
    for i in range(n):
        for j in range(n-i-1):
            if b[j] > b[j+1]:
                b[j],b[j+1] = b[j+1],b[j]
                o.append([2,j+1])
    #discrepancy between a and b 
    for i in range(n):
        if a[i] > b[i]:
            o.append([3,i+1])
    print(len(o))
    for op in o:
        print(*op)


t = int(input())
for _ in range(t):
    solve()
