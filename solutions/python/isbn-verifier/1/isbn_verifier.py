def is_valid(isbn: str) -> bool:
    s = isbn.replace('-', '')
    if len(s) != 10:
        return False

    if not s[:-1].isdigit():
        return False
    if not (s[-1].isdigit() or s[-1] == 'X'):
        return False

    total = sum(int(s[i]) * (10 - i) for i in range(9))
    last = 10 if s[-1] == 'X' else int(s[-1])
    total += last

    return total % 11 == 0
