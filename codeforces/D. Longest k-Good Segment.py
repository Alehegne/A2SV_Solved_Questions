from collections import deque,Counter
n,k = map(int,input().split())

a = list(map(int,input().split()))

left = 0
window = Counter()
# min_deq = deque()#for min in window,increasing
# max_deq = deque()#decreasing
best_left = float("inf")
best_right = float("-inf")

for right,el in enumerate(a):
    #add to the deque for efficienct max and min tracking
    # while max_deq and el >= max_deq[-1]:
    #     max_deq.pop()
    # max_deq.append(el)

    # while min_deq and el <= min_deq[-1]:
    #     min_deq.pop()
    # min_deq.append(el)
    window[el] += 1
    #shrink if invalid
    while len(window) > k and left < n:
        left_ = a[left]
        window[left_] -= 1
        if window[left_] == 0:
            del window[left_]
        # if min_deq and left_ == min_deq[0]:
        #     min_deq.popleft()
        # if max_deq and left_ == max_deq[0]:
        #     max_deq.popleft()
        left += 1
    length = right - left

    # if max_deq and min_deq and abs(len(window) - (max_deq[0]-min_deq[0]+1)) <=1 and length > best_right-best_left:#consequtive
    #     best_left = left
    #     best_right = right
    if length > best_right - best_left:
        best_left = left
        best_right = right

        
print(best_left+1,best_right+1)



