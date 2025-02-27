def main() :
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    lower_case_text = text.lower()
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    character_dict = character_count(lower_case_text)
    print(character_dict)

def get_book_text(path) :
    with open("books/frankenstein.txt") as f :
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import character_count

main()


    