import sys
import os.path
from pathlib import Path
from stats import (
    get_word_count, 
    get_character_count,
    get_character_count_report,
)

def get_book_text(book_path):
    # Make sure a file exists before we try to open it

    # Open the book and read all its contents into memory and return it
    book = Path(book_path)
    book_body = book.read_text()
    return book_body

def main():
    args = sys.argv
    if(len(args) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1] 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    character_count = get_character_count(book_text)
    character_count_report = get_character_count_report(character_count)
    for item in character_count_report:
        print(f"{item[0]}: {item[1]}")

    print("============= END ===============")
    sys.exit(0)


main()