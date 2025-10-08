def translate(text):
    vowels = ["a", "e", "i", "o", "u"]
    extra = ["xr", "yt"]

    def translate_word(word):
        # Rule 1 — starts with a vowel or "xr"/"yt"
        if word[0] in vowels or word[:2] in extra:
            return word + "ay"

        # Rule 3 — starts with consonant(s) followed by "qu"
        # Handle only if "qu" occurs before the first vowel
        for i, ch in enumerate(word):
            if ch in vowels:
                break
            if word[i:i+2] == "qu":
                return word[i+2:] + word[:i+2] + "ay"

        # Rule 2 — standard consonant cluster
        for i, ch in enumerate(word):
            if ch in vowels or word[i:i+2] in extra:
                return word[i:] + word[:i] + "ay"

        # Rule 4 — consonant(s) followed by "y"
        for i, ch in enumerate(word):
            if ch == "y" and i != 0:
                return word[i:] + word[:i] + "ay"

        return word + "ay"

    # Handle multiple words
    return " ".join(translate_word(w) for w in text.split())
