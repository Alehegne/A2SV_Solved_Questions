class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = defaultdict(list)
        for w in strs:
            # key = "".join(sorted(w))
            tup = [0]*26
            # if key not in freq:
            #     freq[key] = []
            for c in w:
                tup[ord(c)-ord('a')]+=1
            freq[tuple(tup)].append(w)
        ans = [val for val in freq.values()]
        return ans






        
