import re
import argparse
from collections import Counter


class TextAnalyzer:
    def __init__(self, text=""):
        self.text = text
        self.words = re.findall(r"\b\w+\b", self.text.lower())

    def load_from_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.text = file.read()
                self.words = re.findall(r"\b\w+\b", self.text.lower())
            print(f"Text loaded from {file_path}")
            return True
        except Exception as e:
            print(f"Error loading file: {e}")
            return False

    def load_text(self, text):
        self.text = text
        self.words = re.findall(r"\b\w+\b", self.text.lower())
        print(f"Text loaded successfully ({len(self.words)} words)")

    def search_word(self, word):
        word = word.lower()

        pattern = r"\b" + re.escape(word) + r"\b"
        matches = re.findall(pattern, self.text.lower())

        print(f"\nSearch results for the word '{word}':")
        print(f"The word '{word}' was found {len(matches)} times in the text.")
        return len(matches)

    def replace_word(self, old_word, new_word):
        pattern = r"\b" + re.escape(old_word) + r"\b"
        new_text = re.sub(pattern, new_word, self.text, flags=re.IGNORECASE)

        count = len(re.findall(pattern, self.text, re.IGNORECASE))

        print(f"\nResults of replacing the word '{old_word}' with '{new_word}':")
        print(f"({count} words have been replaced)\n")
        print(new_text)

        return new_text

    def sort_words(self):
        unique_words = sorted(set(self.words))

        print(f"\nResults of sorting words alphabetically:")
        print(f"Found {len(unique_words)} unique words in the text.\n")

        for i, word in enumerate(unique_words, 1):
            print(f"{i}. {word}")

        return unique_words


def main():
    parser = argparse.ArgumentParser(description="Simple Text Analysis")
    parser.add_argument("-f", "--file", help="Path to the file to be analyzed")
    args = parser.parse_args()

    analyzer = TextAnalyzer()

    if args.file:
        if not analyzer.load_from_file(args.file):
            return
    else:
        print("Please enter the text (press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)

        text = "\n".join(lines)
        analyzer.load_text(text)

    while True:
        print("\n" + "=" * 50)
        print("TEXT ANALYSIS APPLICATION")
        print("=" * 50)
        print("1. Search for a word and count its occurrences")
        print("2. Replace a word")
        print("3. Sort words alphabetically")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            word = input("Enter the word to search for: ")
            analyzer.search_word(word)

        elif choice == "2":
            old_word = input("Enter the word to replace: ")
            new_word = input("Enter the replacement word: ")
            new_text = analyzer.replace_word(old_word, new_word)

            save_option = input("\nDo you want to save these changes? (y/n): ")
            if save_option.lower() == "y":
                analyzer.text = new_text
                analyzer.words = re.findall(r"\b\w+\b", analyzer.text.lower())
                print("Changes have been saved.")

        elif choice == "3":
            analyzer.sort_words()

        elif choice == "4":
            print("Thank you for using this application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
