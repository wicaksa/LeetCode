class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        # edge cases 
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        # main loop
        for i in range(0, len(s) - 1):
            substring = ""
            substring += s[i]
            if len(substring) > longest:
                        longest = len(substring)
            for j in range(i + 1, len(s)):
                if s[j] not in substring: 
                    substring += s[j]
                    if len(substring) > longest:
                        longest = len(substring)
                else:
                    break
        return longest
            
