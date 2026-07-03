class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)          # locate end of the length header
            length = int(s[i:j])        # digits between i and the '#'
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length          # jump to the next header
        return res
