class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        pt1 = 0
        pt2 = len(numbers) - 1

        while True:
            temp = numbers[pt1] + numbers[pt2]
            if temp == target:
                return [pt1 + 1, pt2 + 1]
            elif temp > target:
                pt2 -= 1
            elif temp < target:
                pt1 += 1
            if pt1 == pt2:
                return nul