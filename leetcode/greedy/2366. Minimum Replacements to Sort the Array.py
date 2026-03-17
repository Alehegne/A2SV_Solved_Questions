class Solution:
    def minimumReplacement(self, nums):

        ans = 0
        last = nums[-1]

        for i in range(len(nums)-2, -1, -1):

            curr = nums[i]
            if curr > last:
                #29 8 => 7 7 7 8
                #19 6 => 3 4 6 6 # into 3 parts
                partition = (curr + last - 1)//last #ceil division
                ans += (partition - 1)
                last = curr // partition
            else:
                last = nums[i]
        return ans
