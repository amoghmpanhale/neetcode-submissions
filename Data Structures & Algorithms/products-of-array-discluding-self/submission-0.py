class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(len(nums)):
                if j != i:
                    output[j] *= curr
        return output
