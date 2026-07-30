class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1 #depending if last bit is 1 or 0, if 1, then add to count 1
            n >>= 1 #shift right once (aka removed LSB) and checks next LSB
        return count
            
        