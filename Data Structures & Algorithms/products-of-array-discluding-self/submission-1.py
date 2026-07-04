class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Initialize the arrays
        n = len(nums)
        output = [1] * n
        prefix = [1] * n
        suffix = [1] * n

        # Make the prefix array
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # Make the suffix array
        for i in range(n - 2, -1, -1):
            print(i)
            suffix[i] = suffix[i+1] * nums[i+1]

        print(prefix)
        print(suffix)

        # Do the multiplication
        for i in range(n):
            output[i] = prefix[i] * suffix[i]

        return output 
