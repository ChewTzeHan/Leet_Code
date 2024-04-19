class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        palin = s[0]
        for i in range(len(s)):
            word = s[i]
            count = 1

            for j in range(i+1, len(s)):
                word += s[j]
                
                if word == word[::-1] and len(word) > len(palin):
                    palin = word

        return palin