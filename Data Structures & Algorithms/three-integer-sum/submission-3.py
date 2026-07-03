class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        numbers = sorted(nums)
        output = set()

        for i in range(len(numbers)):
            n = numbers[i]
            pt1 = i + 1
            pt2 = len(numbers) - 1

            target = -1 * n

            while pt1 < pt2:
                sum = numbers[pt1] + numbers[pt2]
                if sum == target and pt1 != i and pt2 != i:
                    output.add((numbers[pt1], numbers[pt2], n))
                    pt1 += 1
                elif sum < target:
                    pt1 += 1
                else:
                    pt2 -= 1
        
        return [list(triplet) for triplet in output]