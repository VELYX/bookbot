import sys
from stats import book_word_counter
from stats import sorting_function

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]

    total_words = book_word_counter(book) 
    sorted_list = sorting_function(book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", book, "...")
    print("----------- Word Count ----------")
    print("Found", total_words, "total words")
    print("--------- Character Count -------") 
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
