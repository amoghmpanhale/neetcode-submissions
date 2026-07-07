class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            
            # mid becomes right if the target is in the left ascending array
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: # check to see if target is in the new array for whether it's the left array or the right one
                    l = mid + 1 # update the left array to make the new one
                else:
                    r = mid - 1
            else: # mid becomes left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1