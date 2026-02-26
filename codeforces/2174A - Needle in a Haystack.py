import sys
input = sys.stdin.readline
from collections import Counter
def solve():
    s= input().strip()
    t = input().strip()
    tc = Counter(t)
    sc = Counter(s)
    t_ = []
    for tk in tc:
        el = [tk]*(tc[tk] - sc[tk])
        t_.extend(el)
    t_.sort()
    sp = 0
    tp = 0
    res = []
    while sp < len(s) and tp < len(t_):
        if sc[s[sp]] > tc[s[sp]]:
            print("Impossible")
            return
        if s[sp] < t_[tp]:
            res.append(s[sp])
            sp += 1
        elif t_[tp] < s[sp]:
            res.append(t_[tp])
            tp += 1
        else:
            #when its equal, greedily choice using the next
            temp_sp = sp
            while s[temp_sp] == t_[tp]:
                if temp_sp == len(s) - 1:
                    break
                temp_sp += 1

            if s[temp_sp] <= t_[tp]:
                res.append(s[sp])
                sp += 1
            else:
                res.append(t_[tp])
                tp += 1          
    #impossible
    for c in s[sp:]:
        if sc[c] > tc[c]:
            print("Impossible")
            return
    res.extend(t_[tp:])
    res.extend(s[sp:])
    # print(res)
    print("".join(res))
t = int(input())
for _ in range(t):
    solve()
