def book_word_counter(book_path):
    words = get_book_text(book_path).split()
    return len(words)

def get_book_text(book_path):
    with open (book_path) as f:
        book_text = f.read()
    return book_text

def main():
    # print(get_book_text("books/frankenstein.txt"))
    print(book_word_counter("books/frankenstein.txt"), "words found in the document")

main()
