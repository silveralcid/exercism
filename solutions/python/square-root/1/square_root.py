def square_root(number):
    if number <= 0:
        raise ValueError("n must be a positive whole number")

    low, high = 1, number

    while low <= high:
        mid = (low + high) // 2
        sq = mid * mid

        if sq == number:
            return mid

        elif sq < number: 
            low = mid + 1
        else: 
            high = mid - 1

    return -1

