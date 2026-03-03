 
n,k,q = map(int,input().split())
recipe = []
min_ = float("inf")
max_ = float("-inf")
# recipe = list(list(map(int,input().split())) for _ in range(n))
for _ in range(n):
    inp = list(map(int,input().split()))
    min_ = min(min_,inp[0],inp[1])
    max_ = max(max_,inp[0],inp[1])
    recipe.append(inp)
 
 
# question = list(list(map(int,input().split())) for _ in range(q))
question = []
for _ in range(q):
    inp = list(map(int,input().split()))
    left = inp[0] - min_
    right = inp[1] - min_
    question.append([left,right])
 
prefix_sum = [0]*(max_-min_+1)
for l,r in recipe:
    prefix_sum[l-min_]+=1
    if r-min_ + 1 < len(prefix_sum):
        prefix_sum[r-min_+1] -= 1
 
for r in range(1,len(prefix_sum)):
    prefix_sum[r] += prefix_sum[r-1]
k_count = [0]*len(prefix_sum)
 
 
for i,p in enumerate(prefix_sum):
    if p >= k:
        k_count[i] = 1
for i in range(1,len(k_count)):
    k_count[i] += k_count[i-1]
ans = []
 
# print(k_count)
for st,en in question:
    if st < 0 and en < 0:
        ans.append(0)
        continue
    if st >= len(k_count):
        ans.append(0)
        continue
    # print("st and end",st,en)
    end = en
    if en > len(k_count)-1:
        end = -1
    if st <= 0:
        ans.append(k_count[end])
    else:
        ans.append(k_count[end] - k_count[st-1])
    
for a in ans:
    print(a)
 
