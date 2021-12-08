"""
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Get k to be less than length of nums 
        # while k > len(nums):
        k = k % len(nums)
        print("k=", k)
        
        while k > 0:
            val = nums.pop(len(nums)-1)
            nums.insert(0, val)
            k = k -1
        
#         # 2. Splice front of nums
#         front = nums[0:k+1]
#         print(f"front = {front}")
        
#         # 3. Splice back of nums
#         back = nums[k+1:]
#         print(f"back = {back}")
        
#         # 4. Return back + front
#         out = back+front 
#         print(out)
#         return out
        
