class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:

        st = []

        pu = "Push"
        po = "Pop"
        idx = 1
        prev = 0
        for i in range(len(target)):
            # while idx != target[i]:
            #     st.push(pu)
            #     idx += 1
            # while st and st[-1] != target[idx-1]:
            #     st.push(po)
            #     st.pop()

            pusha = target[i] - prev - 1
            st.extend([pu]*pusha)
            st.extend([po]*pusha)
            st.append(pu) #push the current
            prev = target[i]
        return st












"""

[1,3,4] 
"""