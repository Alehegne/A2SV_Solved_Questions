class Solution:
    def judgeCircle(self, moves: str) -> bool:

        curr = [0,0]

        for d in moves:
            if d == "L":
                curr[0] -= 1
            elif d == "R":
                curr[0] += 1
            elif d == "U":
                curr[1] += 1
            else:
                curr[1] -= 1
        return curr[0] == 0 and curr[1] == 0
        