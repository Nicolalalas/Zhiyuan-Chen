# Latest commit ID (7 characters long): >>>

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
    # --- YOU CODE STARTS HERE
    pass


def run_tests():
    import doctest
    # Run start tests in all docstrings
    #doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
    
    # Run start tests per function
    #doctest.run_docstring_examples(sum_evens, globals(), name='LAB 0',verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)   

if __name__ == "__main__":
    run_tests()
