def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)

    sorted_list = count_characters(file_contents)
    sorted_list.sort(reverse=True, key=sort_on)
    
    print_report(word_count, sorted_list)

    
    
def count_words(book):
    word_list = book.split()
    counter = 0

    for w in word_list:
        counter += 1

    return counter

def count_characters(book):
    char_dict = {}
    book_to_lower = book.lower()
    character_list = list(book_to_lower)

    for c in character_list:
        if c.isalpha():
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1

    return dict_to_list(char_dict)

def dict_to_list(char_dict):

    char_dict_list=[]

    for c, count in char_dict.items():
        temp_dict = {'char': c, 'num': count}
        char_dict_list.append(temp_dict)

    return char_dict_list

def sort_on(dict):
    return dict["num"]

def print_report(word_count, sorted_list):
    print(f"----Begin report of Frankenstein----\n"
        f"      Total Word Count = {word_count}")
    for i in sorted_list:
        print(f"The character {i['char']} appeared {i['num']} times")

main()

