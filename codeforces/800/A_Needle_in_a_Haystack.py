
from collections import Counter
def solve():
    s = input()
    t = "".join((sorted(input())))
    tf=Counter(t)
    sf=Counter(s)
    #check impossible
    for k in sf.keys():
        if k not in tf:
            print("Impossible")
            return
    visited=Counter()
    r=""
    sidx=0
    for i in range(len(t)):
        if tf[t[i]]>sf[t[i]]:
            r+=t[i]
            if sidx<len(s) and t[i]==s[sidx] and sidx+1<len(s) and s[sidx+1] in visited:
                sf[s[sidx]]-=1
                sidx+=1
                if sf[s[sidx]] == 0:
                    del sf[s[sidx]]
                while sidx<len(s) and s[sidx] in visited:
                    r+=s[sidx]
                    visited[s[sidx]]-=1
                    if visited[s[sidx]]==0:
                        del visited[s[sidx]]
                    sidx+=1            
            tf[t[i]]-=1
            if tf[t[i]]==0:
                del tf[t[i]]
        else:
            if s[sidx]==t[i]:
                r+=t[i]
                #update freq of s
                sf[t[i]]-=1
                if sf[t[i]]==0:
                    del sf[t[i]]
                if sidx<len(s)-1:
                    sidx+=1
                while sidx<len(s) and s[sidx] in visited:
                    r+=s[sidx]
                    visited[s[sidx]]-=1
                    if visited[s[sidx]]==0:
                        del visited[s[sidx]]
                    sidx+=1
                tf[t[i]]-=1
                if tf[t[i]]==0:
                    del tf[t[i]]
            else:
                #add to visited
                tf[t[i]]-=1
                if tf[t[i]]==0:
                    del tf[t[i]]
                visited[t[i]]+=1

    if visited:
        r+=s[sidx]
        sidx+=1
        visited[s[sidx]]-=1
        if visited[s[sidx]]==0:
            del visited[s[sidx]]
    print(r)
t = int(input())
for _ in range(t):
    solve()