


t=int(input())
from collections import Counter
for _ in range(t):

    n=int(input())
    s=Counter(map(int,input().split()))

    # if len(s)<=2:
    #     keys=list(s.keys())
    #     # print(keys)
    #     if len(keys)==2:
    #         diff=abs(s[keys[1]]-s[keys[0]])
    #         if diff<=1:
    #             print("Yes")
    #         else:
    #             print("No")
    #     else:
    #         print("Yes")

    # else:
    #     print("No")

    if len(s)>2:
        print("No")
    else:
        vals=list(s.values())
        print("Yes" if max(vals)-min(vals)<=1 else "No")
