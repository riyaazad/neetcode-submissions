class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seenMap:
                return [seenMap[diff], i]
            seenMap[num] = i