class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        # max_left[i] = tallest bar in height[0..i]
        max_left = [0] * n
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])

        # max_right[i] = tallest bar in height[i..n-1]
        max_right = [0] * n
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        # Water above each bar is bounded by the shorter wall
        total_water = 0
        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            total_water += water_level - height[i]

        return total_water