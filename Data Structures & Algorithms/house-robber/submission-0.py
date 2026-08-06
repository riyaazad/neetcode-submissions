class Solution:
    def rob(self, nums: List[int]) -> int:

        #intuitivetly, you would think to sum up every other index
        #but this doesnt work in [1,9,1,1,9,1] cuz OPT = 19
        #look back at the last subproblem: n-1, n-2

        for i in range(1, len(nums)): #start after 0 index cuz it returns its own
            if i ==1:
                nums[i]= max(nums[i], nums[i-1])
            else:
                nums[i]= max(nums[i] + nums[i-2], nums[i-1])
        return nums[-1] #return the last element in nums cause it will have the max amount

        