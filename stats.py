def get_word_count(input_string):
    words = input_string.split()
    return len(words)

def get_character_count(input_string):
    character_count_dict = {}

    for c in input_string.lower():
        if c in character_count_dict:
            character_count_dict[c] += 1
        else:
            character_count_dict[c] = 1
    return character_count_dict

def get_character_count_report(character_count_dict):
    report = list(filter(filter_alphanumeric, character_count_dict.items()))
    report.sort(reverse=True, key=sort_on_value)
    
    return report

def filter_alphanumeric(keyValue):
    return keyValue[0].isalpha()

def sort_on_value(keyValue):
    return keyValue[1]