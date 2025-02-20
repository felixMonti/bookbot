def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    character_count = count_char(file_contents)
    print_report(word_count,character_count)
    

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count    

def sort_on(dict):
    # Helper function to sort the list of dictionaries by the "num" key
    return dict["num"]

def print_report(word_count, character_counts):
    # Print the report header
    print("--- Begin report of books/frankenstein.txt ---")
    # Print the word count
    print(f"{word_count} words found in the document\n")

    alpha_counts = [{"char": char, "num": count} for char, count in character_counts.items() if char.isalpha()]
    alpha_counts.sort(reverse=True, key=sort_on)
    for entry in alpha_counts:
        print(f"The '{entry['char']}' character was found {entry['num']} times")

    print("--- End report ---")

    
if __name__ == "__main__":
    main()
