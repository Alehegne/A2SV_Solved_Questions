class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:


        f = Counter()
        for res in responses:
            # for w in set(res):
            #     f[w]+=1
            f.update(set(res))
        # items = sorted(f.keys(),key = lambda x:(-f[x],x))
        max_ = max(f.values())
        # print(items)
        # return items[0]
        return min([k for k,v in f.items() if v==max_])


        
