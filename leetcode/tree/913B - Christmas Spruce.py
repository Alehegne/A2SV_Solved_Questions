
n = int(input())
adj_list = [[] for _ in range(n+1)]

for i in range(2,n+1):
    p = int(input())
    adj_list[p].append(i)

for v in adj_list:
    if not v:
        continue
    cnt = 0
    for el in v:
        if not adj_list[el]:
            cnt += 1
    if cnt < 3:
        print("No")
        exit()
print("Yes")
