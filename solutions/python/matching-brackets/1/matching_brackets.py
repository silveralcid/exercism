def is_paired(input_string: str) -> bool:
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    openings = set(pairs.values())
    stack = []

    for ch in input_string:
        if ch in openings:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0
