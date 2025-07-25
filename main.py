import sys
from stats import num_of_words, character_count, sort_dictionary, prepare_report

def get_book_text(bookPath):
    with open(bookPath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    textPath = sys.argv[1]
    text = get_book_text(textPath)
    word_count = num_of_words(text)
    char_dict = character_count(text)
    sorted_chars = sort_dictionary(char_dict)

    report = prepare_report(word_count, sorted_chars)
    print(report)

main()