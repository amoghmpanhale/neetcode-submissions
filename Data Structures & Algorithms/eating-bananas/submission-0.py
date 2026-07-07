class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            # Check to see if this number works to finish the bananas in time
            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            
            if time <= h:
                high = mid
            else:
                low = mid + 1

        return low