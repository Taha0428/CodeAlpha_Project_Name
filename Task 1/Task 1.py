import random
from colorama import Fore, Style, init

init(autoreset=True)

def play_game():
    choices = ['Islamabad', 'Karachi', 'Rawalpindi', 'Lahore', 'Wazirabad', 'Gujrat']
    selected_word = random.choice(choices)
    guessed_letters = []
    tries = 6
    display = ['_'] * len(selected_word)

    print(Fore.CYAN + "Welcome to the Word Guessing Game!")

    while tries > 0 and '_' in display:
        print("\n" + Fore.GREEN + "Current word: " + ' '.join(display))
        print(Fore.YELLOW + f"Tries remaining: {tries}")
        print(Fore.MAGENTA + "Letters guessed: " + ', '.join(guessed_letters))

        guess = input(Fore.BLUE + "Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print(Fore.RED + "You've guessed that before. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in selected_word.lower():  
            for index, letter in enumerate(selected_word.lower()):  

                if letter == guess:
                    display[index] = selected_word[index] 
            print(Fore.GREEN + "Nice guess!")
        else:
            tries -= 1
            print(Fore.RED + "Wrong guess!")

    if '_' not in display:
        print(Fore.GREEN + "\nWell done! You found the word: " + selected_word)
    else:
        print(Fore.RED + "\nGame over! The word was: " + selected_word)

if __name__ == "__main__":
    play_game()