def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(count_words(file_contents))
    print(count_characters(file_contents))
    



def count_words(book):
    word_list = book.split()
    counter = 0

    for w in word_list:
        counter += 1

    return counter

def count_characters(book):
    character_dictionary = {}
    book_to_lower = book.lower()
    character_list = list(book_to_lower)

    for c in character_list:
        if c in character_dictionary:
            character_dictionary[c] += 1
        else:
            character_dictionary[c] = 1

    return character_dictionary

main()

