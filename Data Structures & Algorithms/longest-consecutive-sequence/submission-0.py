class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        contains = set(nums)
        max_len = 0
        for n in nums:
            if n-1 in contains: continue
            curr_length = 0
            
            curr = n
            while curr in contains:
                curr +=1
                curr_length +=1
                
            max_len = max(curr_length, max_len)
        return max_len


        