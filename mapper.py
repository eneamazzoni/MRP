import hashlib

BIP39 = [line.strip() for line in open('bip39_wordlist.txt')]

def to_bip39(word):
    word = word.lower()
    if word in BIP39:
        return word
    # Fallback: first letter → first BIP39 word with that letter
    letter = word[0]
    for w in BIP39:
        if w.startswith(letter):
            return w
    return "abandon"  # safety

# Test
print(to_bip39("hobbit"))  # → "happy"
