def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_counts = get_character_counts(book_text)
    character_counts_sorted_list = character_counts_dictionary_to_sorted_list(character_counts)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for item in character_counts_sorted_list:
        if not item["character"].isalpha():
            continue
        print(f"The '{item["character"]}' character was found {item["count"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    character_counts = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def character_counts_dictionary_to_sorted_list(character_counts):
    sorted_list = []
    for character in character_counts:
        sorted_list.append({
                "character": character,
                "count": character_counts[character]})
    sorted_list.sort(reverse=True, key=lambda item: item["count"])
    return sorted_list

main()
