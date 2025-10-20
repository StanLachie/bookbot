from stats import count_total_words, count_characters, format_char_counts
import sys

def read_book_file(book_path):
    with open(book_path) as book:
        return book.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = read_book_file(book_path)
    num_words = count_total_words(book_text)
    char_counts = count_characters(book_text)
    formated = format_char_counts(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in formated:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")




main()
