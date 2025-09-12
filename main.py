import sys
from stats import get_num_words, get_number_characters, print_sorted_report

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    get_num_words()
    get_number_characters()
    print_sorted_report()
    
    
if __name__ == '__main__':
    main()