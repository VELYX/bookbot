from stats import book_word_counter
from stats import character_counter

def main():
    # print(get_book_text("books/frankenstein.txt"))
    print(book_word_counter("books/frankenstein.txt"), "words found in the document")
    char_counts = character_counter("books/frankenstein.txt")
    print(char_counts)

main()
