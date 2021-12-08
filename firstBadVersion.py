# 278
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.

"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [true]
        # [false, false, false, true, true, ]
        # find the lowest index of true 
        
        # keep track of the lowest index: set it to the highest value + 1
        lowest_index = 2**31 # 2147483648
        
        # keep track of mid, low, high 
        low  = 1
        high = n+1
        mid  = low + high // 2
        
        # keep track of index seen with a set 
        seen = set()
        
        # while mid is not in set 
        while mid not in seen:
            
            # add mid to seen
            seen.add(mid)
            print("seen", mid, seen)
        
            # if value at mid is false: 
            if isBadVersion(mid) == False:
            
                # low = mid
                low = mid
                
                # recalculate mid 
                mid = (low + high) // 2
                
            # if value at mid is true: 
            elif isBadVersion(mid) == True:
                
                # save lowest index of true 
                if mid <= lowest_index:
                    lowest_index = mid
                    
                print("lowest index =", lowest_index)
                
                # high = mid 
                high = mid
                
                # recalculate mid
                mid = (low + high) // 2
                
            print("mid=", mid, isBadVersion(mid))
            
        # return lowest index  
        return lowest_index
