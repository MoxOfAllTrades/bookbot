def word_count(text):
    return len(text.split())

def char_count(text):
    char_dict = {}
    for word in text.lower().split():
        for c in word:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    return char_dict

def sorted_dict_list(char_dict):
    dict_list = []
    for k,v in char_dict.items():
        dict_list.append({"char":k,"num":v})
    dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list