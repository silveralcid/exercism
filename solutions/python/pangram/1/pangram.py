def is_pangram(sentence):
    chars = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    if all (c in sentence for c in chars):
        return True
    else:
        return False
