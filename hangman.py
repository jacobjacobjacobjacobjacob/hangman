import random


def menu():
    # Initialize the variables for wins and losses
    wins = 0
    losses = 0

    while True:
        # Prompt the user to select an option and convert it to lowercase
        menu_choice = input('Type "play" to start the game, "results" to view the scoreboard, or "exit" to quit: ').lower()

        if menu_choice == 'play':
            # Start the hangman game and update the wins and losses variables
            wins, losses = play_hangman(wins, losses)
        elif menu_choice == 'results':
            # Display the results by showing the number of wins and losses
            display_results(wins, losses)
        elif menu_choice == 'exit':
            # Exit the program
            break
        else:
            # Handle invalid menu options
            print('Invalid menu option. Please try again.')
            continue


def display_results(wins, losses):
    # Print the number of wins and losses
    print(f'You have won: {wins} times.')
    print(f'You have lost: {losses} times.')


def play_hangman(wins, losses):
    # Number of attempts allowed
    attempts = 8

    # List of words that can be chosen for the game
    word_list = ['python', 'java', 'swift', 'javascript']

    # Select a random word from the list
    correct_word = random.choice(word_list)
    masked_word = "-" * len(correct_word)

    print('Welcome to Hangman!')
    print(f'Guess the word in {attempts} attempts to win.')

    # Function to update the masked word based on user input
    def update_masked_word(word, masked_word, char):
        new_masked_word = ''
        for i in range(len(masked_word)):
            if word[i] == char:
                new_masked_word += char
            else:
                new_masked_word += masked_word[i]
        return new_masked_word

    # Get user input until the word is guessed or attempts run out
    while masked_word != correct_word:
        print(masked_word)
        if attempts != 0:
            user_input = input('Input a letter: ')

            # Checking if the player only inputs a single letter
            if len(user_input) != 1:
                print('Please enter a single letter.')
                continue

            # Only accept lowercase English letters
            if not user_input.islower() or user_input not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a lowercase letter from the English alphabet.')
                continue

            # Check if the letter is already guessed
            if user_input in masked_word:
                print("You've already guessed this letter.")
                continue

            # Check if the letter appears in the word
            if user_input not in correct_word:
                print("That letter doesn't appear in the word.")
                attempts -= 1

            masked_word = update_masked_word(correct_word, masked_word, user_input)

            if attempts == 0:
                print('You lost!')
                losses += 1
                break

    if masked_word == correct_word:
        print(f'You guessed the word {correct_word}!')
        print('You survived!')
        wins += 1

    return wins, losses


# Start the hangman game menu
menu()
