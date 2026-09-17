class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        contains = set(nums) #we dont care for repeats/order
        max_count = 0
        for n in nums:
            if n-1 in contains: continue #if number exists before, then n shouldnt be our starting point so skip
            curr_length = 0 #inside for loop bc it should be reset for each n

            curr = n
            while curr in contains:
                curr +=1
                curr_length +=1
            
            max_count = max(max_count, curr_length)
        return max_count


        