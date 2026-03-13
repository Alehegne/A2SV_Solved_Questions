class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key = lambda x: (abs(x[0]-x[1])),reverse=True)
        print(costs)
        n = len(costs)

        c_a = n//2
        c_b = n//2
        cost = 0

        for ca,cb in costs:
            if (c_a and ca <= cb) or not c_b:
                cost += ca
                c_a -= 1
            else:
                cost += cb
                c_b -= 1
        return cost









        
