t=int(input())

for _ in range(t):
    n=int(input())
    keys=list(map(int,input().split()))
    our_key=0
    for i in range(1,4):
        if i not in keys:
            our_key=i
    count=1
    found_key=keys[our_key-1]
    while found_key:
        count+=1
        found_key=keys[found_key-1]
        if count==3:
            print("YES")
            break
    else:
        print("NO")

