from stats import get_num_words, get_number_characters

def main():
    """
    Prints the number of words in the book "Frankenstein".
    
    Prints the number of distinct characters in the book "Frankenstein".
    """
    words = get_num_words()
    print(f"{words} words found in the document")
    
    characters = get_number_characters()
    
    for char in characters:
        print(f"'{char}': {characters[char]}, ")
    


    
if __name__ == '__main__':
    main()