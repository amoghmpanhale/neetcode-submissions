class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        left = ""
        right = ""

        for left_pointer in range(len(s)):

            right_pointer = len(s) - left_pointer - 1
            
            left_char = s[left_pointer].lower()
            right_char = s[right_pointer].lower()

            if left_char.isalnum():
                left += left_char

            if right_char.isalnum():
                right += right_char

        
        
        return left == right