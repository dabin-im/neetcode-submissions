class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            area = r - l
            if heights[l] <= heights[r]:
                area *= heights[l]
                l += 1
            else: 
                area *= heights[r]
                r -= 1
            max_area = max(max_area, area)
        
        return max_area
