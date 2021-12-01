"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.

"""
def atoi(s):
    # Read in and ignore any white space: strip() removes leading whitespaces.
    a = s.strip()
    # print("a =", a)

    # Edge case if all whitespaces are stripped and a has a length of 0
    if len(a) == 0:
      return 0

    # Check for sign whether it's positive or negative. 
    # Check first element and see if it's - or +.

    # Assume number is positive 
    sign = 1

    if a[0] == "-": 
      sign = -1 
      a = a[1:]
    elif a[0] == "+": # s[0] == "+":
      # sign is already positive
      a = a[1:]

    # create a variable to store new string
    output = ""

    # Read in next the characters until the next non-digit character or the end of the input is reached. string.isnumeric()    
    for c in a:
      #print("c", c)
      if c.isnumeric():
          output += c
      else: # False 
          # The rest of the string is ignored.
          break 

    # If no digits were read, then the integer is 0. 
    if len(output) == 0 or output == "-" or output == "+": 
      return 0
    else: 
      # Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
      # Change the sign as necessary (from step 2).
      digit = int(output) * sign

    # Make sure result is within the range 
    if digit < -2**31: 
      return -2**31
    elif digit > 2**31-1:
      return 2**31-1
    else: 
      return digit 

def main(): 
    str1 = "-42"
    str2 = "   -42"
    str3 = "words and 987"
    str4 = "-91283472332"
    str5 = "4193 with words"

    print(f"{str1} : {atoi(str1)}")
    print(f"{str2} : {atoi(str2)}")
    print(f"{str3} : {atoi(str3)}")
    print(f"{str4} : {atoi(str4)}")
    print(f"{str5} : {atoi(str5)}")

if __name__ == "__main__": 
    main()

