class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1

        max_container = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            max_container = max(area, max_container)
            if heights[left]<=heights[right]: #already calculated max area, so we're just deciding if we should move to next index as long as left isnt larger than right
                left+=1
            else:
                right-=1
        return max_container

        
        