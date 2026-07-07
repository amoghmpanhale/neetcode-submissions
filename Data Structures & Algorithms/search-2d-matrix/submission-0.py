class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        full = []
        for l in matrix:
            full += l
        
        low = 0
        high = len(full)

        while low < high:
            mid = (low + high) // 2

            if full[mid] == target:
                return True
            elif full[mid] > target:
                high = mid
            else:
                low = mid + 1
        return False