import random

def choose_word():
    # Define words by category
    words_by_category = {
        "Animals": ["dog", "cat", "bird", "elephant", "giraffe", "lion"],
        "Fruits": ["apple", "banana", "orange", "grape", "strawberry"],
        "Colors": ["red", "blue", "green", "yellow", "orange", "purple"]
    }
    # Choose a random category
    category = random.choice(list(words_by_category.keys()))
    # Choose a random word from the selected category
    word = random.choice(words_by_category[category])
    return category, word

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "-"
    return displayed_word
def main():
    print("Welcome to the Word Guessing Game!")
    category, word = choose_word()
    guessed_letters = []
    num_guesses = len(word)

    print("Category:", category)
    print("Word:", display_word(word, guessed_letters))

    while num_guesses > 0:
        guess = input("Guess the word: ").lower()
        num_guesses -= 1

        if guess == word:
            print("Congratulations! You guessed the word '{}' in {} guesses.".format(word, len(word) - num_guesses))
            break
        else:
            print("Incorrect guess.")
            # Reveal one letter for each incorrect guess except the last one
            if num_guesses > 0:
                unrevealed_letters = [letter for letter in word if letter not in guessed_letters]
                revealed_letter = random.choice(unrevealed_letters)
                guessed_letters.append(revealed_letter)
                print("Hint:", display_word(word, guessed_letters))
            else:
                print("The word was:", word)

if __name__ == "__main__":
    main()
