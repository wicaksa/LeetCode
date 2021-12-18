"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

"""



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # edge cases 
        
        # create output list
        output = []
        
        # iterate through the list 
        for i in range(0, len(numbers)):
        
            # diff = target - numbers[i]
            difference = target - numbers[i]
            
            # count the occurence, if it's in the list 
            if numbers.count(difference) != 0: 
            
            # if the occurrence is not zero:
                # remove the current index
                numbers.remove(numbers[i])
            
                # get the index
                index = numbers.index(difference) + 1
                
                # add current index to list
                output.append(i + 1)
                
                # add occurence index to list
                output.append(index + 1)
                
                # break
                break
            
        # add one to each element
        
        # return 
        return output
            
                
        
