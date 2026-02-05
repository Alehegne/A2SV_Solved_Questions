
# def find_nth_occurence(s,char,n):
#     count=0
#     for i,c in enumerate(s):
#         if c==char:
#             count+=1
#             if count==n:
#                 return i
#     return -1
# def checkOrder(x,s):

#     nth=1
#     xidx=find_nth_occurence(x,s[0],nth)

#     if xidx==-1:
#         return False
#     sidx=0
#     while sidx<len(s)-1:
#         xidx=(xidx+1)%len(x)
#         sidx=sidx+1
#         if s[sidx]!=x[xidx]:
#             nth+=1
#             xidx=find_nth_occurence(x,s[0],nth)
#             if xidx==-1:
#                 return False
#             sidx=0
#     return True     

# t=int(input())
# for _ in range(t):
#     xn,sn=map(int,input().split())
#     x=input()
#     s=input()
#     #check order
#     isInOrder = checkOrder(x,s)
#     if not isInOrder:
#         print(-1)
#         continue
#     ops=0
#     if s in x:
#         print(0)
#         continue
#     while True:
#         x+=x
#         ops+=1
#         if s in x:
#             break

#     # print("x:",x)
#     if s in x:
#         print(ops)
#     else:
#         print(-1)



t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()

    # Step 1: feasibility check
    repeat = (len(s) // len(x)) + 2
    if s not in x * repeat:
        print(-1)
        continue

    # Step 2: count operations
    cur = x
    ops = 0
    while s not in cur:
        cur += cur
        ops += 1

    print(ops)
