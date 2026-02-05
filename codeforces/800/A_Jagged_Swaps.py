t=int(input())

for _ in range(t):

    n=int(input())

    s=list(map(int,input().split()))
    # cont=True
    # while cont:
    #    cont=False
    #    for i in range(1,len(s)-1):
    #          if s[i-1]<s[i] and s[i]>s[i+1]:
    #             s[i],s[i+1]=s[i+1],s[i]
    #             cont=True
    # print("YES" if s==sorted(s) else "NO")

    #cleaner
    print("YES" if s[0]==1 else "NO")