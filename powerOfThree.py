def powerThree(n): 
    # checks if parameter is a power of three
    # input : integer n 
    # output: boolean 
    
    if n < 0 : 
        return False
        
    exponent = 0
    product  = 0
    
    while product < n: 
        product = 3**(exponent)
        if product == n:
            return True
        else:
            exponent += 1
    
    return False

def main(): 
    n1 = 27 # True
    n2 = 4  # False 
    
    print(f"should be True for 27: {powerThree(n1)}")
    print(f"should be False for 4: {powerThree(n2)}")

if __name__ == "__main__": 
    main()
