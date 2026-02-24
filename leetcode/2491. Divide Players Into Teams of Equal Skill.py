class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        s = sum(skill)
        h = len(skill)//2
        if s % h:
            return -1
        each = s//h
        
        # sk = Counter(skill)
        score = 0
        skill.sort()
        l, r = 0,len(skill) - 1
        while l<r:
            if skill[l] + skill[r] != each:
                return -1
            score += skill[l] * skill[r]
            l += 1
            r -= 1
        return score
        
            

            
        

        
