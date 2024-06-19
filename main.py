def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(count_words(file_contents))



def count_words(book):
    word_list = book.split()
    counter = 0

    for w in word_list:
        counter += 1

    return counter



main()

