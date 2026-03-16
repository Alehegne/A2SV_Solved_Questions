class Solution:
    def numRabbits(self, answers: List[int]) -> int:


        cnt = Counter(answers)
        ans = 0

        for k in cnt:
            val = (cnt[k]//(k+1))*(k+1)
            addened = (k+1) if cnt[k] % (k+1) != 0 else 0
            ans +=(val+addened)
        return ans
        
