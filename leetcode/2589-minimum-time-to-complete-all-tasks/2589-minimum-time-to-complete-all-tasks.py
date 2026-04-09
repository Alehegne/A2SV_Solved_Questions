class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:

        tasks.sort(key = lambda x: x[1])

        taken = []
        visited = set()

        # print(tasks)

        for s,e,d in tasks:
            l = bisect.bisect_left(taken,s)
            r = bisect.bisect_right(taken,e)

            # print("left:",l,"right:",r)

            rem = d - (r-l)

            # print(f"start:{s,e,d}","rem:",rem,"time:",len(taken))


            temp = e
            took = []
            while rem > 0:
                while temp in visited:
                    temp -= 1
                visited.add(temp)
                took.append(temp)
                rem -= 1
            # taken.extend(took[::-1])
            #merge taken with took
            took.reverse()
            i = j = 0
            temp = []
            while i < len(taken) and j < len(took):
                if taken[i] < took[j]:
                    temp.append(taken[i])
                    i += 1
                else:
                    temp.append(took[j])
                    j += 1
            temp.extend(taken[i:])
            temp.extend(took[j:])
            taken = temp

            # print(f"taken:{taken}","rem:",rem,"time:",len(taken),"vis:",visited,"took:",took)

        return len(taken)
        