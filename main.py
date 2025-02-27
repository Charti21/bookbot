def main() :
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

def get_book_text(path) :
    with open("books/frankenstein.txt") as f :
        file_contents = f.read()
    return file_contents

def count_words(text) :
    word_list = text.split()
    num_words = len(word_list)
    return num_words

main()
    
    