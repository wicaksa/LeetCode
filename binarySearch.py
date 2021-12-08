# 704 Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # keep track of seen indexes with set() -> lookup time == 0(1)
        seen = set()
        
        # get length of nums
        L = len(nums)
        
        # get current midpoint
        # get max point and low point
        mp = L // 2
        minp = 0
        maxp = L
        
        # while mp not in seen
        while mp not in seen:
            # add midpoint to seen 
            seen.add(mp)
            
            # get element at that midpoint
            n = nums[mp]
            
            # if the target == element: 
            if target == n: 
                
                # return the index 
                return mp 
            
            # elif the target > element 
            elif target > n : 
            
                # calculate new mp, lowpoint, maxpoint
                minp = mp
                mp = (maxp + minp) // 2
            
            # elif the target < element 
            elif target < n : 
            
                # calculate the new mp, lowpoint, maxpoint
                maxp = mp 
                mp = (maxp + minp) // 2
                
        # return -1 if element is not found
        return -1 
        
