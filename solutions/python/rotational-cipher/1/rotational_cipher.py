def rotate(text, key):

    result = ""

    for char in text:
        if char.islower():
            shifted = chr((ord(char) - 97 + key) % 26 + 97)
            result += shifted
        elif char.isupper():
            shifted = chr((ord(char) - 65 + key) % 26 + 65)
            result += shifted
        else:
            result += char
    return result
    