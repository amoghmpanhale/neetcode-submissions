class Solution:
    def isValid(self, s: str) -> bool:

        open = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                open.append(s[i])
            else:

                if len(open) == 0:
                    return False
                    
                op = open.pop()

                if op == '(' and s[i] != ')':
                    return False
                elif op == '[' and s[i] != ']':
                    return False
                elif op == '{' and s[i] != '}':
                    return False
        
        if len(open) > 0:
            return False

        return True