class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Understand 
            # Calculate running sum of the input which is a list.
            # Input: list
            # Output: list with running sum 
        # Matching
            # Similar to fib 
        # Plan
            # Input: [1,2,3,4]
            # Output: [1,3,6,10]
            # Running Sum: [1, 1+2, 1+2+3, 1+2+3+4].
            # [1, nums[0] + 2, nums[1] + 3, nums[2] + 4].
        # Implement 
            # pointer1 at 0, pointer2 at 1
            # traverse through input 
                # set the value of nums[pointer2] to nums[pointer1] + nums[pointer2]
            # return the list 
            # check edge cases 
            
#         # Solution 1 : 
#         # Create pointer
#         previousValue = 0
        
#         # Edge cases
#         if len(nums) == 0 or len(nums) == 1:
#             return nums
        
#         for currentValue in range(1, len(nums)):
#             nums[currentValue] = nums[previousValue] + nums[currentValue]
#             previousValue = previousValue + 1
#         return nums
    
        # Cleaned up Solution
        for currentValue in range(1, len(nums)):
            nums[currentValue] += nums[currentValue - 1]
        return nums
        
