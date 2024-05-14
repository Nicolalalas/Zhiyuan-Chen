# Latest commit ID (7 characters long): >>>c4a1883

def sum_evens(num_list):
    """
        >>> sum_evens([1,5,-3,5,359,8,14,-25,1000])
        1022.0
        >>> sum_evens([14,5,-3,5,9,8,14,7,-846])
        -810.0
        >>> sum_evens([-8,-4,1,2,3,4,5,6,12])
        12.0

        To verify output is being returned, not printed
        >>> output = sum_evens([1,5,-3,5,45,8,-5,500,6,-25])
        >>> output
        514.0
    """
    total = 0.0  
    for num in num_list:
        if num % 2 == 0:  
            total += num
    return total

def run_tests():
    import doctest
    
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
    
    
