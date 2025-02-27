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

def sort_characters(character_count_dict) :
    character_list = []
    for character, count in character_count_dict.items():
        character_dict = {character:count}
        character_list.append(character_dict)
    
    def sort_on(character_dict) :
        return list(character_dict.values())[0]
    
    
    character_list.sort(reverse=True, key=sort_on)
    return character_list



    
    