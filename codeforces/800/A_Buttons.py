
def solve():

    a,b,c=list(map(int,input().split()))
    if a>b:
        print("First")
    elif b>a:
        print("Second")
    else:
        if c%2==0:
            print("Second")
        else:
            print("First")

t = int(input())
for _ in range(t):
    solve()