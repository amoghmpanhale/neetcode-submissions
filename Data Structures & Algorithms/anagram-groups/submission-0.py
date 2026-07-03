class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = {}
        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted in chars:
                chars[word_sorted].append(word)
            else:
                chars[word_sorted] = [word]
        output = []
        for char in chars:
            output.append(chars[char])
        return output