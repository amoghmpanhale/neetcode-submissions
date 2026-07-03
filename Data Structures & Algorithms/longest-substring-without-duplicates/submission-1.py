class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encountered = {}

        left = 0
        right = 0

        output = 0

        while right < len(s):
            
            if s[right] in encountered and encountered[s[right]] + 1 > left:
                left = encountered[s[right]] + 1

            encountered[s[right]] = right

            if right - left + 1 > output:
                output = right - left + 1

            right += 1

        return output