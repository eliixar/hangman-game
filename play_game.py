from word_generator import generate_word
from display_hangman import display_hangman

def play_game():
    print("Welcome to the hangman game!")


    word = generate_word() # generate the word and store it
    guessed_letters = set() # keep track of guessed letters

    incomplete_word = "_" * len(word) # start with the amount of blank spaces neededY
    

    while True:
        choose_chances = input("Would you like to choose the number of chances? Y / N \n").upper().strip()

        if choose_chances == "Y":
            user_choice = input("Please enter a number from 1 to 9:\n")

            if user_choice.isnumeric() and 1 <= int(user_choice) <= 9:
                chances = int(user_choice)
                break
            else:
                print("Invalid Input. Please enter a number from 1 to 9:\n")

        elif choose_chances == "N":
            chances = 6
            break

        else:
            print("Invalid input. Please enter Y or N.\n")
            continue
        
    print(incomplete_word)


    while chances > 0:
        guess = input("Please guess a letter! ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter one alphabetical character only.\n")
            continue # guess again
       
        if guess in guessed_letters:
            print("You already guessed that letter! Try again.\n")
            continue

        guessed_letters.add(guess) # add the guess to the set of guessed letters

        if guess in word:
            print("Good job! The letter " + guess + " is in the word!")
            incomplete_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
            display_hangman(chances)
            print(incomplete_word)

        else:
            print("Sorry, the letter " + guess + " is not in the word!")
            chances -= 1 # decrement number of chances left
            display_hangman(chances)
            print(incomplete_word)

        if "_" not in incomplete_word:
            print("Congratulations! The word was: " + word)
            print("You won with " + str(chances) + " chances remaining!")
            chances = -1
            retry = input("Would you like to start a new game? Y / N\n")
            if retry.upper() == "Y":
                play_game()
            else:
                chances = -1
                print("Thank you for playing!")

    if (chances == 0):
        print("Sorry! You have lost the game.")
        print("The word was" , word)
        chances = -1
        retry = input("Would you like to start a new game? Y / N\n")
        if retry.upper() == "Y":
            play_game() # restart game
        else:
            chances = -1 # exit loop
            print("Thank you for playing!")


play_game()