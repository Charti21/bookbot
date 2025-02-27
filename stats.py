def count_words(text) :
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def character_count(lower_case_text) :
    character_count_dict={}
    for character in lower_case_text :
        if character in character_count_dict :
            character_count_dict[character] += 1
        else :
            character_count_dict[character] = 1
    return character_count_dict
    