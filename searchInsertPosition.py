# 35. Search Insert Position

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

"""

import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # input : nums: sorted list, target: int
        # output: int of index of target or where it should be 
        
        # create a variable to check if you've seen the index 
        seen = set()
        
        
        # calculate low, mid, high
        low  = 0 
        high = len(nums)
        mid  = (low + high) // 2 
        
        # while not in seen:
        while mid not in seen:
        
            # add to seen 
            seen.add(mid)
            
            # case if target matches number
            if target == nums[mid]:
            
                # return mid
                return mid
            
            # case if target > number 
            if target > nums[mid]:
            
                # low = mid
                low = mid
                
                # mid = high + low // 2
                mid = (low + high) // 2
            
            # case if target < number 
            elif target < nums[mid]: 
            
                # high = mid 
                high = mid
                
                # mid = high + low // 2
                mid = (low + high) // 2
            
        # return mid 
        print(low, high, math.ceil((low+high) / 2))
        return math.ceil((low+high) / 2)
        
