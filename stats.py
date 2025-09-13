def get_num_words(text):
    words_count = text.split()
    return len(words_count)

def get_char_count(text):
    text = text.lower()
    char_count = {
        "t":0,
        "p":0,
        "c":0
    }
    for char in text:
        if char == "t":
            char_count["t"] += 1
        elif char == "p":
            char_count["p"] += 1
        elif char == "c":
            char_count["c"] += 1
    return char_count