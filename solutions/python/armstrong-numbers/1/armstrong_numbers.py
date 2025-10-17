def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    count = len(digits)
    return sum(d ** count for d in digits) == number