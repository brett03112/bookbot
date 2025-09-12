def get_book_text(book_path):
    """
    Returns the text of a book from a file.

    Args:
        book_path (str): The path to the text file containing the book.

    Returns:
        str: The text of the book.
    """
    with open(book_path) as f:
        return f.read()
    

def get_num_words():
    """
    Returns the number of words in the book "Frankenstein".

    Returns:
        int: The number of words in the book.
    """
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    
    count = 0
    for word in book_text.split():
        count += 1
        
    return count

def get_number_characters():
    """
    Returns the number of characters in the book "Frankenstein".

    Returns:
        dict: A dictionary with the characters of the book as keys and the
        number of times they appear as values.
    """
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path).replace(" ", "").replace("\n", "").lower()
    characters = {}
    
    for char in book_text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    
    return characters
