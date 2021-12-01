# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

import string 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # create a list of alphabet characters 
        a = string.ascii_lowercase
        
        # loop through each character in the alphabet list and store the lowest index into the list
        # if there are no letters that appear only once, add a -1 
        x = [s.find(c) for c in a if s.count(c) == 1] or [-1]
        
        # return the lowest value in the list which represents the lowest index of first unique character
        return min(x)
        
        
        #         # iterate through s 
        #         for i in range(0, len(s)):

        #             # count each element 
        #             # if count == 1, return the current index
        #             if s.count(s[i]) == 1: 
        #                 return i

        #         # return -1
        #         return -1
       
                
        
