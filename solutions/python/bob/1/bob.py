def response(hey_bob):

    hey_bob = hey_bob.strip()
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif not hey_bob.strip():
        return "Fine. Be that way!"
    else:
        return "Whatever."