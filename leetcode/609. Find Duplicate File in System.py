class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:


        freq = {}
        # content: []
        for path in paths:

            dirs = path.split()
            dir_ = dirs[0]
            for i in range(1,len(dirs)):
                ind = dirs[i].index("(")
                file_name = dirs[i][:ind]
                content = dirs[i][ind+1:len(dirs[i])-1]
                file_path = f"{dir_}/{file_name}"
                # if content not in freq:
                #     freq[content] = []
                # freq[content].append(file_path)
                freq.setdefault(content,[]).append(file_path)
        # ans = []
        # for k, v in freq.items():
        #     if len(v)>1:
        #        ans.append(v)
        # print(ans)
        # return ans
        return [v for k,v in freq.items() if len(v) > 1]

        