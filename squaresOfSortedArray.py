"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # create two pointers
        p1 = 0
        p2 = len(nums) - 1 
        
        # create empty output array 
        output = []
        
        # while p1 < p2: 
        while p1 <= p2:
        
            # if abs p1 > abs p2 : 
            if abs(nums[p1]) > abs(nums[p2]):

                # add p1^2 to the output at index 0 
                output.insert(0, nums[p1]**2)

                # increment p1
                p1 += 1

            # else if abs p2 > abs p1
            else: # abs(num2) > abs(num1):

                # add p2^2 to the output at index 0 
                output.insert(0, nums[p2]**2)

                # decrement p2
                p2 -= 1 
        
        # return output
        return output
