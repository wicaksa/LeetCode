# LeetCode 459. Repeated Substring Pattern
# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
                
        # Get length of string 
        LENGTH = len(s)
        # print("length =", LENGTH)

        # Edge Case
        if LENGTH < 2: 
            return False

        # Get midpoint
        midpoint = LENGTH // 2

        # Get endpoint 
        endpoint = 1

        # Get times to multiply substring
        amount = LENGTH

        # While endpoint is less than midpoint 
        while endpoint <= midpoint:
            #print("endpoint =", endpoint)
            #print("midpoint =", midpoint)

            # Get substring 0 to endpoint 
            substring = s[0:endpoint]
            #print("substring = ", substring)

            # If substring * times == s 
            if substring * amount == s:

                # Return True 
                return True

            # Else if False 
            else:

                # Increment End Point
                endpoint += 1

                # Change times 
                amount = LENGTH // endpoint
        return False
