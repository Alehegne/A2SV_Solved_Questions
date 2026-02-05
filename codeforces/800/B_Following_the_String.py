
t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split(" ")))
    output=""
    visited={}
    #val:freq
    asci=97
    for i in range(len(nums)):

        if nums[i]==0:
            output+=chr(asci)
            visited[chr(asci)]=1
            asci+=1
        else:

            for key in visited.keys():
                if visited[key]==nums[i]:
                    output+=key
                    visited[key]+=1
                    break
    print(output)

