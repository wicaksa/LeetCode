class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. UNDERSTAND
            # Input:  int array nums[], int target
            # Output: int array of indices that add up to the two numbers 
            # Each input has exactly one solution
            # Not allowed to use same elements twice
            # Return answer in ANY order
        # 2. Matching 
            # Traversing thru arrays
        # 3. Planning
            # Two pointers
                # One at first element
                # Sec at second element
            # Iterate the first pointer
                # Iterate the second pointer through the array
                    # check if it's less than target
                        # if yes, check if first pointer + second pointer values == 9
                            # if it is return the idexes
                    # move the second pointer
        # 4. Implementation
        p1 = 0
        p2 = 0
        answer = []
        
        for p1 in range(0, len(nums)):             # O(N)
            val1 = nums[p1]
            
            for p2 in range(0, len(nums)):         # O(N)
                if (p1 != p2):
                    val2 = nums[p2]
                    if (val1 + val2 == target):
                        answer = [p1, p2]
                        return answer
        # 5. Review
            # nums = [2,7,11,15], target = 9
            # [0,1]
            
            # p1 val1 p2 nums[p2] target
            # 0.  2.  0.            9
            # 0.  2.  1.   7.       9 
            
        # 6. Evaluate
            # O(n^2) pretty slow 
