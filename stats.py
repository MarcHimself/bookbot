def get_num_words(text):
    words_count = text.split()
    return len(words_count)

def get_char_count(text):
    text = text.lower()
    # empty dict
    char_count = {}
    for char in text:
        # check if the character is a letter
        if char.isalpha():
            # if its already part of the dictionnary add 1    
            if char in char_count: 
                char_count[char] += 1
            # if its not part of the dictionnary set it to 1
            elif char not in char_count:
                char_count[char] = 1
    return char_count

def sort_dictionnary(unsorted_dict):
    sorted_list = sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_list)
    return sorted_dict

def print_report(total_words, sorted_dict, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")
