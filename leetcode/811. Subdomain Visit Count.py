class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        freq = Counter()
        for dom in cpdomains:

            for i in range(len(dom)-1, 0,-1):
                if dom[i]==".":
                    freq[dom[i+1:]]+=int(dom[:dom.index(" ")])
                elif dom[i]==" ":
                    freq[dom[i+1:]]+=int(dom[:dom.index(" ")])
                    break

        ans = []
        for k,v in freq.items():
            ans.append(f"{v} {k}")
        return ans


        