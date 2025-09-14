from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path) 
    num_words = get_num_words(text)
    char_dict = get_char_count(text)
    sorted_char_dict = sort_dictionnary(char_dict)
    print_report(num_words, sorted_char_dict, book_path)
    
def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

main()