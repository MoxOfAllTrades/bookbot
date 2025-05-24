from stats import char_count, sorted_dict_list, word_count
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(path, num_words, num_chars, dict_list):
    print(f"============ BOOKBOT ============\nAnalyzing book found at: {path}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words.")
    print(f"--------- Character Count -------")
    for each in dict_list:
        if each["char"].isalpha():
            print(f"{each["char"]}: {each["num"]}")
    print("============= END ===============")

def main():
        
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>\nPlease specify a valid book path for the bot to analyze.")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
        num_words, num_chars = word_count(text), char_count(text)
        dict_list = sorted_dict_list(num_chars)
        return print_report(path, num_words, num_chars, dict_list)

main()