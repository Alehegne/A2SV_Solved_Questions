class Solution:
    def customSortString(self, order: str, s: str) -> str:

        f = Counter(s)

        new_ = ""
        for o in order:
            if o in f:
                new_ += (o*f[o])
                del f[o]
        for k in f:
            new_ += (k*f[k])
        return new_

        
