class DSU:
    def __init__(self, n):
        self.parent = list(range(n))  # Initialize parent array
        self.size = [1] * n  # Initialize size array for union by size

    def find(self, x):
        if self.parent[x] != x:  # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            # Union by size
            if self.size[rootA] < self.size[rootB]:
                self.parent[rootA] = rootB
                self.size[rootB] += self.size[rootA]
            else:
                self.parent[rootB] = rootA
                self.size[rootA] += self.size[rootB]

    def printGroups(self):
        groups = defaultdict(list)
        for i in range(len(self.parent)):
            root = self.find(i)
            groups[root].append(i)
        return list(groups.values())
    def countGroups(self):
        groups = set()
        for i in range(len(self.parent)):
            groups.add(self.find(i))
        return len(groups)

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        """
        given: unique nums
           - len(nums) nodes,
           - edge between nums[i] and nums[j] if common factor
        - in short:- merges nodes with a common factor than 1
        [4,6,15,35] => (4,6),(6,15),(15,35)
        [20,50,9,63] => (20,50),(9,63)
        [20,15,22,40] => (20,15),(20,22),(20,40)
        n^2 = to get members (bottleneck)
        - for a certain n:- find another number with it n has common factor
        - x = 15, options = [20,40]
        - factors of 15 = (3,5,15):- 3:15,5:15,15:15
        - factors of 20 = (2,4,5,10,20): 2:20,4:20,10:20,20:20
        """

        def factors(n):
            ff = set()
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    ff.add(i)
                    ff.add(n//i)
            ff.add(n)
            return ff
        
        f = {}
        dsu = DSU(len(nums))
        #time complexity:- 10000 *100 
        for i in range(len(nums)):
            fac = factors(nums[i])
            # print("fact of :",nums[i],"is:",fac)
            for e in fac:
                if e in f:
                    dsu.union(i,f[e])
                else:
                    f[e] = i
        groups = dsu.printGroups()
        mx = float("-inf")
        for gr in groups:
            mx = max(mx,len(gr))
        return mx
        


        
