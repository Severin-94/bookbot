def main():
    book_path = "books/frankenstein.txt"
    text = get_file(book_path)
    #print(text)

    word_count = count_words(book_path)
    #print(word_count)

    characters = character_count(text)
    #print (characters)

    val = split_dict(characters)

    sorted = sort_for_count(val)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document \n")
    print_how_often(sorted)
    print("--- End report ---")
    



def get_file(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(book_path):
    text = get_file(book_path)
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def character_count(text):
    lower_text = text.lower()
    real_count = {}
    for character in lower_text:
        if character in real_count:
            real_count[character] += 1
        else:
            real_count[character] = 1
    return real_count

def split_dict(dictionary):
    dict_list = []
    for key in dictionary:
        if key.isalpha():
            dict_list.append({"letter": key, "num" : dictionary[key]})
    return(dict_list)

def sort_key(dict):
    return dict["num"]

def sort_for_count(list_of_dicts):
    list_of_dicts.sort(reverse=True, key=sort_key)
    return list_of_dicts

def print_how_often(list_of_dicts):
    for entry in list_of_dicts:
        print(f"The \'{entry["letter"]}\' was found {entry["num"]} times")

main()
