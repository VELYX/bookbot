from stats import book_word_counter
from stats import sorting_function

def main():
    book = "books/frankenstein.txt"
    # print(get_book_text("books/frankenstein.txt"))
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
