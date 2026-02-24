class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        b = 0
        n = len(people)
        i,j = 0,n-1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            b += 1
            j -= 1
        return b

        


