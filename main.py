from stats import *
import sys

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for dictionary in chars_sorted_list:
        if not dictionary["char"].isalpha():
            continue
        print(f"{dictionary["char"]}: {dictionary["num"]}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_word_count(book)
    char_counts = get_char_count(book)
    chars_sorted_list = sort_char_count(char_counts, True)
    print_report(book_path,num_words, chars_sorted_list)


main()