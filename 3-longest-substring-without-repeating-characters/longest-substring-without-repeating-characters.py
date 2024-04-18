class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = [0, '']
        string = ''
        
        for i in range(len(s)):
            count = 1
            string = s[i]
            
            for j in range(i+1, len(s)):
                if s[j] not in string:
                    string += s[j]
                    count += 1
                else:
                    break
            
            if count > longest[0]:
                longest = [count, string]
                
        print(longest)
        
        return longest[0]