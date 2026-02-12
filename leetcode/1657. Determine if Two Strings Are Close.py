class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        n1 = len(word1)
        n2 = len(word2)


        f1 = Counter(word1)
        f2 = Counter(word2)
        #early termination if there is char mismatch
        for k in f1:
            if k not in f2:
                return False
        for k in f2:
            if k not in f1:
                return False


        #freq to char with that freqe map
        fr1 = Counter()
        fr2 = Counter()
        for k,v in f1.items():
            fr1[v]+=1
        for k,v in f2.items():
            fr2[v]+=1

        for k,v in fr1.items():
            if fr2[k]!=v:
                return False
        return True
        


        
