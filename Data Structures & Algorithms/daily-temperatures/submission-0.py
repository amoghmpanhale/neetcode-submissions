class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)

        output = [0] * n

        for i in range(n):

            curr = temperatures[i]

            for j in range(i, n):
                if temperatures[j] > curr:
                    print(temperatures[j], curr)
                    output[i] = j - i
                    break

        return output