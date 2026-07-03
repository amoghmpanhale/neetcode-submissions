class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        max_count = 0
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > max_count:
                max_count = counts[num]
        
        counts_array = [[] for _ in range(max_count)] 
        for num in counts:
            counts_array[counts[num] - 1].append(num)

        output = []
        for i in range(len(counts_array) - 1, -1, -1):
            for j in range(len(counts_array[i]) - 1, -1, -1):
                output.append(counts_array[i][j])
            if len(output) == k:
                break
        return output