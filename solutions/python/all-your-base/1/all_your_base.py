def rebase(input_base, digits, output_base):

    value = 0
    result = []
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")

    # convert from input_base to base 10
    
    for d in digits:
        if  d < 0 or d >= input_base:
            raise ValueError ("all digits must satisfy 0 <= d < input base")
        else:
            value = value * input_base + d

    # handle zero case
    if value == 0:
        return [0]
            
    # convert from base 10 to output_base
    while value > 0:
        remainder = value % output_base
        result.insert(0, remainder)
        value //= output_base

    return result
        
            
            