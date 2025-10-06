def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    factors  = []

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    for i in range (1, number):
        if number % i == 0:
            factors.append(i)
            
    aliquot = sum(factors)

    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    elif aliquot < number:
        return "deficient"
