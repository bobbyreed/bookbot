from stats import num_of_words
from stats import character_count
from stats import sort_dictionary

def get_book_text(bookPath):
    with open(bookPath) as f:
        file_contents = f.read()
        num_of_words(file_contents)
        return character_count(file_contents)

def main():
    get_book_text('./books/frankenstein.txt')

main()