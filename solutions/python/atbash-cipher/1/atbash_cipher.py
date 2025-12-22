# Atbash mapping (lowercase only)
ATBASH_LOWER = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "zyxwvutsrqponmlkjihgfedcba",
)

def encode(plain_text: str) -> str:
    # Normalize to lowercase
    text = plain_text.lower()

    # Remove punctuation/spaces: keep only letters and digits
    kept_chars = []
    for ch in text:
        if ch.isalnum():
            kept_chars.append(ch)
    cleaned = "".join(kept_chars)
    
    # Apply Atbash to letters (digits are not mapped, so they stay the same)
    encoded = cleaned.translate(ATBASH_LOWER)
    
    # Group into chunks of 5 characters, separated by spaces
    groups = []
    for i in range(0, len(encoded), 5):
        groups.append(encoded[i:i + 5])
    return " ".join(groups)

def decode(ciphered_text):
    return "".join(ciphered_text.translate(ATBASH_LOWER).split())
    

