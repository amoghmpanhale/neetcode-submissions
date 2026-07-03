class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            seen[num] = 0
        for num in nums:
            seen[num] += 1
            if seen[num] > 1:
                return True
        return False