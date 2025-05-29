from stats import count_words, count_characters, sort_count

def get_book_text(file_path):
    """
    Function get_book_text: takes in the file path of a book's text, and returns the text found in that file
    
    Input:
        file_path (string): a string containing the file path referencing a .txt file
        eg: "directory/book.txt"

    """

    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def print_report(file_path):
    """
    Prints the required report on a given book's text, including word and character count
    """
    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    char_count = sort_count(count_characters(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in char_count:
        #print(d)
        if d['char'].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============= END ===============")



import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    print_report(book_path)


# call Main to execute
main()