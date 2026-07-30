class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]: #check after first element (the rest)
        #! either extend the subarray or start new from current num (if bigger)
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
        return max_sum

#this is kadanes algorithm