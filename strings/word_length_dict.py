"""
    Determines the length of each word in a string and puts the word and its length in a dictionary
"""

def word_length_dict(text):
    d = {e: len(e) for e in text.split(" ")}
    return d

text = "The quick brown fox jumps over the lazy dog"
print(word_length_dict(text))
