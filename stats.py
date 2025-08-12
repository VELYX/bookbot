def get_book_text(book_path):
    with open (book_path) as f:
        book_text = f.read()
    return book_text

def book_word_counter(book_path):
    words = get_book_text(book_path).split()
    return len(words)

def character_counter(book):
    char_counts = {}
    lowercase_char = character.lower()
    for lowercase_char in book:
        if character in char_count:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
        return char_counts
            
