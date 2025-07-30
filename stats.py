def get_word_count(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    char_count_dict = {}
    chars = list(book)
    for char in chars:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sort_on(items):
    return items["num"]

def sort_char_count(dictionary, reverse_order):
    dict_list = []
    for value in dictionary:
        new_dict = {}
        new_dict["char"] = value
        new_dict["num"] = dictionary[value]
        dict_list.append(new_dict)

    dict_list.sort(reverse=reverse_order, key=sort_on)
    return dict_list