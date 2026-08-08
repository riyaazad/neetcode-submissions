class Solution:
    def climbStairs(self, n: int) -> int:
        #index 0-> only 1 way to get there, stay on floor
        #index 1 -> step 1, only 1 way to get there with step 1
        #index 2 -> 2 ways to get there, (1+1 or 2)
        #initilize that array then
        ways = [1,1,2] 

        #range does not include last element, but len(n) does only if array, but for n = int, have to do n+1
        for i in range (3, n+1): #i = steps
            ways.append(ways[i-1] + ways[i-2])
        return ways[n]