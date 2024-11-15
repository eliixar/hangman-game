from word_generator import generate_word
from display_hangman import display_hangman

def play_game():
    print("Welcome to the hangman game!")

    word = generate_word() # generate the word and store it
    chances = 6 # initially have 6 chances to guess the word
    guessed_letters = set() # keep track of guessed letters

    incomplete_word = "_" * len(word) # start with the amount of blank spaces needed


    while chances > 0:
        guess = input("Please guess a letter! ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter one alphabetical character only.")
            continue # guess again
       
        if guess in guessed_letters:
            print("You already guessed that letter! Try again.")
            continue

        guessed_letters.add(guess) # add the guess to the set of guessed letters

        if guess in word:
            print("Good job! The letter " + guess + " is in the word!")
            incomplete_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
            display_hangman(chances)
            print(incomplete_word)

        else:
            print("Sorry, the letter " + guess + " is not in the word!")
            chances -= 1
            display_hangman(chances)
            print(incomplete_word)

        if "_" not in incomplete_word:
            print("Congratulations! The word was: " + word)
            print("You won with " + str(chances) + " chances remaining!")

  

    if (chances == 0):
        print("The word was" , word)


play_game()