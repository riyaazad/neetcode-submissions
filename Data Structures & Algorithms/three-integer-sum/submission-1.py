class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        used = set()
        res =[]

        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
    
                k = nums[i] + nums[j]
                target = -(nums[i] + nums[j])

                #or could do:
                #k2 = abs(k) if k<0 else -k 
                
                #to find the number that makes it 0
                
                hash = tuple(sorted([nums[i], nums[j], target]))

                if target in seen and hash not in used: 
                    #** important for no repetition
                    res.append([nums[i], nums[j], target])
                    used.add(hash)
            seen.add(nums[i])
            
        return res