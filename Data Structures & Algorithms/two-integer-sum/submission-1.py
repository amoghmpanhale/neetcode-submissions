class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairings = {}
        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            if pair in pairings:
                return sorted([i, pairings[pair][1]])
            pairings[pair] = (num, i)
            pairings[num] = (pair, i)
        return []
