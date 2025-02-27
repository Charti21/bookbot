def main() :

    path = "books/frankenstein.txt"
    text = get_book_text(path)
    lower_case_text = text.lower()
    num_words = count_words(text)
    #print(f"{num_words} words found in the document")
    character_count_dict = character_count(lower_case_text)
    #print(character_count_dict)
    character_list = sort_characters(character_count_dict)
    #print (character_list)

    # Print Report
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #Putting Each Result on a Seperate Line Formatting
    for character_dict in character_list :
        for character, count in character_dict.items() :
            if character.isalpha() :
                print(f"{character}: {count}")
    print("============= END ===============")

def get_book_text(path) :
    with open("books/frankenstein.txt") as f :
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import character_count
from stats import sort_characters

main()


    