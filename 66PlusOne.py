class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # take an array of ints -> convert to a number -> add +1 
        
        # input: non-empty array 
        # output: non-empty array +1 
        # no empty array, smallest size = 1
        
        # convert digit [] to int
        string_digit = [str(i) for i in digits] # convert to list of strings
        string_digit = "".join(string_digit) # join the elements into a string
        int_digit = int(string_digit) # convert the string into an int
        
        # add 1 
        int_digit += 1
        
        # convert back to a list
        new_digit = [int(x) for x in str(int_digit)]
        
        #return the new list 
        return new_digit
