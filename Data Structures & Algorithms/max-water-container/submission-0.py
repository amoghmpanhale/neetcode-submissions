class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        pt1 = 0
        pt2 = len(heights) - 1

        max = 0

        while pt1 < pt2:

            height = min(heights[pt1], heights[pt2])
            width = pt2 - pt1
            area = height * width

            if area > max:
                max = area

            if heights[pt1] > heights[pt2]:
                pt2 -= 1
            else:
                pt1 += 1
        
        return max